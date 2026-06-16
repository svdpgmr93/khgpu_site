from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='education'

urlpatterns = [
    path('edu-programs-catalog/', get_edu_catalog, name='edu_catalog'),
    path('edu-program/', get_edu_program, name='edu_program'),
]
