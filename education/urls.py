from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='education'

urlpatterns = [
    path('edu-programs-catalog/', get_edu_catalog, name='edu_catalog'),
    path('edu-program/<int:program_id>', edu_program, name='edu_program'),
    path('program-bak-cards', get_edu_bak_cards, name='get_edu_bak_cards'),
    path('program-mag-cards', get_edu_mag_cards, name='get_edu_mag_cards'),
    path('searching_bak', searching_bak),
    path('searching_mag', searching_mag),
]
