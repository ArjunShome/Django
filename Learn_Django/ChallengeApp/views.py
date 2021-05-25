from django.shortcuts import render
from django.http import HttpResponse
from ChallengeApp.models import Individual,Gadget,Individual_Gadget_Detail

# Create your views here.

def index(requests):
    my_dict = {'Name':'Arjun Shome'}
    return render(requests, 'ChallengeApp/index.html', context=my_dict)


def details(requests):
    detail_list = Individual_Gadget_Detail.objects.order_by('Buy_Date')
    data = {'user_details':detail_list}
    return render(requests, 'ChallengeApp/GadgetDetails.html', context=data)
