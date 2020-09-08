from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'streamhunt/home.html')


def profile(request):
    return render(request, 'streamhunt/profile.html')


def randomizer(request):
        
        list_of_streamers = ['aardvarkjon', 'monstercat', 'ninja', 'everywheresean']
        streamer = random.choice(list_of_streamers)
        context = {'streamer' : streamer }
        return render(request, 'streamhunt/randomizer.html', context)

