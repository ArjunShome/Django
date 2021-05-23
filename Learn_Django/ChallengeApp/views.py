from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requests):
    my_dict = {'Name':'Arjun Shome'}
    return render(requests, 'ChallengeApp/index.html', context=my_dict)
