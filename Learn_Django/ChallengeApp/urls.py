from django.urls import path
from ChallengeApp import views

app_name = 'challenge'

urlpatterns=[
  path('', views.index, name='index'),
  path('details/', views.details, name='details'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout,name="logout"),
  path('users/', views.user_display, name="users")
]
