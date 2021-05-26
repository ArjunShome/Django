from django import forms
from ChallengeApp.models import Individual

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Individual
        fields = '__all__'
