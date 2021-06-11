from django import forms
from django.contrib.auth.models import User
from ChallengeApp.models import Individual_Detail

class DateInput(forms.DateInput):
    input_type = 'date'

class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class NewUserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = Individual_Detail
        fields = ('User_Img','Address','State','Country','PinCode','MobileNumber','Gender','DOB')
        widgets = {
            'DOB': DateInput()
        }
