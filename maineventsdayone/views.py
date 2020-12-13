from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    days=MainDayOne.objects.all()[0]
    day=Dayone.objects.all()
    events=Event.objects.all()
    return render(request, "maineventsdayone/index.html", {
        "days": days,
        "day":day,
        "events":events,
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def event(request, event):
    days=MainDayOne.objects.all()[0]
    oday=Dayone.objects.all()
    tday=Dayone.objects.get(name=dayone)
    events=Event.objects.all()
    tevent=Dayone.objects.get(name=dayone).events.get(name=event)
    
    return render(request, "home/event.html", {
        "days": days,
        "day": oday,
        "tday": tday,
        "events": events,
        "event": tevent,
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })