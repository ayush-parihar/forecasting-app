from django.urls import path
from . import views
 
app_name = "forecaster"
 
urlpatterns = [
    path("", views.index, name="index"),
    path("predict/", views.predict_view, name="predict"),
]