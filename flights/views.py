from django.http import HttpResponse, HttpResponseNotFound
import flights
from django.shortcuts import render
from .models import Flight, Passenger

# Create your views here.
def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {"flights": flights})

def flight(request, flight_id):
    
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html", {"flight": flight, "passengers": passengers})
