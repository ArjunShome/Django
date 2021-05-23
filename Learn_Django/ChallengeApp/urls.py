from django.urls import path
from ChallengeApp import views

urlpatterns=[
  path('', views.index, name='index'),
]
