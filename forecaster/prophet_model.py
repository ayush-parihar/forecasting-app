"""
Isolated training / inference utilities for Facebook Prophet.
"""
from pathlib import Path
import pandas as pd, joblib
from prophet import Prophet
 
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "daily_sales.csv"
MODEL_PATH = Path(__file__).with_suffix(".pkl")
 
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    df = df.rename(columns={"date": "ds", "sales": "y"})
    return df.sort_values("ds").dropna()
 
def train(save: bool = True):
    df = load_data()
    model = Prophet(interval_width=0.9)
    model.fit(df)
    if save:
        joblib.dump(model, MODEL_PATH)
    return model
 
# Keep a singleton in memory
_model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else train()
 
def forecast(periods: int = 30) -> pd.DataFrame:
    """
    Returns dataframe with ['ds','yhat','yhat_lower','yhat_upper'].
    """
    future = _model.make_future_dataframe(periods=periods)
    fc = _model.predict(future)
    return fc[["ds", "yhat", "yhat_lower", "yhat_upper"]]