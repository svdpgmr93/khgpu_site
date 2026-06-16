from django.shortcuts import render
from .models import EduProgram


def get_edu_catalog(request):
    programs = EduProgram.objects.all()
    return render(request, 'edu-programs-catalog.html', context={'programs': programs})

def get_edu_program(request):
    return render(request, 'edu-program.html')
