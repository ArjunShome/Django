from django.shortcuts import render
from ChallengeApp.models import Individual_Gadget_Detail,User
from ChallengeApp.forms import NewUserForm,NewUserProfileInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate


# Create your views here.

def index(requests):
    my_dict = {'Name':'Arjun Shome'}
    return render(requests, 'ChallengeApp/index.html', context=my_dict)


def details(requests):
    detail_list = Individual_Gadget_Detail.objects.order_by('Buy_Date')
    data = {'user_details':detail_list}
    return render(requests, 'ChallengeApp/GadgetDetails.html', context=data)


def signup(requests):
    
    registered = False

    if requests.method == 'POST':
        userform = NewUserForm(data=requests.POST)
        userprofileform = NewUserProfileInfoForm(requests.POST, requests.FILES)

        if userform.is_valid() and userprofileform.is_valid():
            
            user = userform.save()
            user.set_password(user.password)
            user.save()

            userprofile = userprofileform.save(commit=False)
            userprofile.User = user
            userprofile.User_Img = userprofileform.files['User_Img']
            userprofile.save()

            registered = True

        else:
            print(userform.errors, userprofileform.errors)
    else:
        userform = NewUserForm()
        userprofileform = NewUserProfileInfoForm()

    return render(requests, 'ChallengeApp/Signup.html', context={'user':userform,
                                                                 'userprofile':userprofileform,
                                                                 'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('challenge:index'))


@login_required
def user_display(requests):
    user_list = User.objects.order_by('username')
    data = {'user_list':user_list}
    return render(requests, 'ChallengeApp/UserList.html', context=data)


def user_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('challenge:index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE!!!')
        else:
            print(f'SOMEONE WITH {username} and {password} TRIED TO LOGIN!!')
            return HttpResponse('INVALID LOGIN DETAILS SUPPLIED!!!')
    else:
        return render(request, 'ChallengeApp/login.html', {})
