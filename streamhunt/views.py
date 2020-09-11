from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

from .streamerList import list_of_streamers

def home(request):
    return render(request, 'streamhunt/home.html')


def profile(request):
    return render(request, 'streamhunt/profile.html')


def randomizer(request):
        
        
        streamer = random.choice(list_of_streamers)
        context = {'streamer' : streamer }
        return render(request, 'streamhunt/randomizer.html', context)

