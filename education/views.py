from django.shortcuts import render
from .models import EduProgram, EduProgramEduForm, EduProgramAdvantageText, Suitable, KeySkills, ProgramStructure, Position, Perspective


def get_edu_catalog(request):

    programs_bak = EduProgram.objects.filter(level__contains='Бакалавриат')
    programs_mag = EduProgram.objects.filter(level__contains='Магистратура')
    print(request.GET)

    return render(request, 'edu-programs-catalog.html', context={'programs_bak': programs_bak, 'programs_mag': programs_mag})

def edu_program(request, program_id):
    program = EduProgram.objects.get(id=program_id)
    epef=EduProgramEduForm.objects.filter(edu_program=program_id)
    advantage = EduProgramAdvantageText.objects.filter(op=program_id)
    suitable = Suitable.objects.filter(op=program_id)
    key_skills = KeySkills.objects.filter(op=program_id)
    structure = ProgramStructure.objects.filter(op=program_id)
    position = Position.objects.filter(op=program_id)
    perspective = Perspective.objects.filter(op=program_id)
    return render(request, 'edu-program.html', context={
        'program':program, 
        'epef':epef, 
        'advantage': advantage, 
        'suitable': suitable, 
        'key_skills': key_skills, 
        'structure': structure,
        'position': position,
        'perspective': perspective 
        })
