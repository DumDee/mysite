from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Song


def homepage(request):
    songlist = Song.objects.all()
    context = {'xox': songlist}
    return render(request, "HomePage.html", context)

def about(request):
    return HttpResponse('Go Home, Dude')
