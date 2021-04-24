from django.urls import path
from users import views

urlpatterns = [
    path("", views.index, name="index"),   
    path("login", views.login_view, name="login"),
    path("logout", views.logout, name="logout"),
]