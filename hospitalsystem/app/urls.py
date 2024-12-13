from django.urls import path
from .import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('registration', views.registration, name='registration'),
    path('admindashboard', views.admindashboard, name='admindashboard'),

]