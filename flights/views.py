import flights
from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    flights = Flight.objects.all()
    for flight in flights:
        print(f"{flight.id}: {flight.origin} to {flight.destination}")
    return render(request, "flights/index.html", {"flights": flights})