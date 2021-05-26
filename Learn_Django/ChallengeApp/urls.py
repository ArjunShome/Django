from django.urls import path
from ChallengeApp import views

urlpatterns=[
  path('', views.index, name='index'),
  path('details/', views.details, name='details'),
  path('signup/', views.signup, name='signup')
]
