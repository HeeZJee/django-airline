from django.urls import path
from flights import views

urlpatterns = [
    path("", view.index, name="index")   
]