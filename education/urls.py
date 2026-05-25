from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='education'

urlpatterns = [
    path('', include('education.urls', )),
]
