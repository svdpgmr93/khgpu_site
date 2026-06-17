from django.shortcuts import render
from .models import EduProgram


def get_edu_catalog(request):
    programs_bak = EduProgram.objects.filter(level__contains='Бакалавриат')
    programs_mag = EduProgram.objects.filter(level__contains='Магистратура')
    return render(request, 'edu-programs-catalog.html', context={'programs_bak': programs_bak, 'programs_mag': programs_mag})

def edu_program(request, program_id):
    program = EduProgram.objects.get(id=program_id)
    return render(request, 'edu-program.html', context=program)
