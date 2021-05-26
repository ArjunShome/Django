from django.shortcuts import render
from ChallengeApp.models import Individual,Gadget,Individual_Gadget_Detail
from ChallengeApp.forms import NewUserForm

# Create your views here.

def index(requests):
    my_dict = {'Name':'Arjun Shome'}
    return render(requests, 'ChallengeApp/index.html', context=my_dict)


def details(requests):
    detail_list = Individual_Gadget_Detail.objects.order_by('Buy_Date')
    data = {'user_details':detail_list}
    return render(requests, 'ChallengeApp/GadgetDetails.html', context=data)

def signup(requests):
    form = NewUserForm()
    if requests.method == 'POST':
        form = NewUserForm(requests.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(requests)

        else:
            print('ERROR ADDING USER')
    return render(requests, 'ChallengeApp/Signup.html', context={'form':form})
