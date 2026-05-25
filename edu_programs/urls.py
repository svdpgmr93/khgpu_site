from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'edu_programs'

urlpatterns = [
    path('edu-programs/', edu_programs, name='edu_programs'),
]
