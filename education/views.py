from django.shortcuts import render
from .models import EduProgram


def get_edu_catalog(requests):
    program = EduProgram.objects.get(pk=1)
    return render(requests, 'edu-programs-catalog.html', context={'program': program})