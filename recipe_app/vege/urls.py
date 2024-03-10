from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("home/recipe",views.receipes, name="receipes"),
    path("home/update_recipe/<id>",views.update_recipe, name="receipes"),
    path("home/delete_recipe/<id>",views.update_recipe, name="receipes"),

    
]