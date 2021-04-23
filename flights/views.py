from django.http import HttpResponse, HttpResponseNotFound
import flights
from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {"flights": flights})

def flight(request, flight_id):
    flights = Flight.objects.all()
    for flight in flights:
        if flight_id == flight.id:
            return HttpResponse(f"Flight {flight.id}: {flight.origin} to {flight.destination}")
        else:
            return HttpResponseNotFound(f"No Flight Found!")