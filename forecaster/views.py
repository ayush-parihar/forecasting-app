from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd, plotly.graph_objs as go
from .prophet_model import load_data, forecast
 
def _plot_history(df: pd.DataFrame) -> str:
    fig = go.Figure(go.Scatter(x=df["ds"], y=df["y"], mode="lines",
                               name="Historical sales"))
    return fig.to_html(full_html=False)
 
def _plot_forecast(df_hist: pd.DataFrame, df_fc: pd.DataFrame) -> str:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_hist["ds"], y=df_hist["y"],
                             mode="lines", name="Historical"))
    fig.add_trace(go.Scatter(x=df_fc["ds"], y=df_fc["yhat"],
                             mode="lines", name="Forecast"))
    # shaded CI
    fig.add_trace(go.Scatter(
        x=pd.concat([df_fc["ds"], df_fc["ds"][::-1]]),
        y=pd.concat([df_fc["yhat_upper"], df_fc["yhat_lower"][::-1]]),
        fill="toself", line=dict(width=0), name="90 % CI"))
    return fig.to_html(full_html=False)
 
def index(request):
    return render(request, "forecaster/index.html")
 
def predict_view(request):
    horizon = int(request.GET.get("horizon", 30))
    df_hist = load_data()
    df_fc = forecast(horizon).tail(horizon)
    return JsonResponse({
        "hist": {
            "x": df_hist["ds"].tolist(),
            "y": df_hist["y"].tolist()
        },
        "forecast": {
            "x": df_fc["ds"].tolist(),
            "yhat": df_fc["yhat"].tolist(),
            "lower": df_fc["yhat_lower"].tolist(),
            "upper": df_fc["yhat_upper"].tolist()
        }
    })