from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meetings


def welcome(request):
    # return HttpResponse("Welcome to the meeting planner!")
    return render(request, "website/welcome.html",
                  # {"num_meetings": Meetings.objects.count(), })
                  {"meetings": Meetings.objects.all(), })


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("I'm Daniel and I'm currently working at iMio near Namur, Wallonia, Belgium.")
