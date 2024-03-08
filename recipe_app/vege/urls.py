from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("home/recipe",views.receipes, name="receipes")
]