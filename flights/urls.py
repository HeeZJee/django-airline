from django.urls import path
from flights import views
import flights

urlpatterns = [
    path("", views.index, name="index"),   
    path("<int:flight_id>", views.flight, name="flight")
]