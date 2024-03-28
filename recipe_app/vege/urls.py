from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("home/recipe",views.receipes, name="receipe"),
    path("home/update_recipe/<id>",views.update_recipe, name="update_receipe"),
    path("home/delete_recipe/<id>",views.delete_recipe, name="delete_receipe"),
    path("home/login",views.login_page, name="login"),
    path("home/register",views.register_page, name="register"),
    path("home/logout",views.logout_page, name="logout"),

    
]