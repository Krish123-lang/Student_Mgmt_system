from django.urls import path
from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
]
