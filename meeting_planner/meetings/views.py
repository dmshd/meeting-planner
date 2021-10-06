from django.shortcuts import render, get_object_or_404

from .models import Meetings


def detail(request, id):
    # meeting = Meetings.objects.get(pk=id)
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})