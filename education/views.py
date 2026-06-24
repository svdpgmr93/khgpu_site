from django.shortcuts import render
from .models import EduProgram, EduProgramEduForm, EduProgramAdvantageText, Suitable, KeySkills, ProgramStructure, Position, Perspective

def get_edu_catalog(request):

    programs_bak = EduProgram.objects.filter(level__contains='Бакалавриат')
    programs_mag = EduProgram.objects.filter(level__contains='Магистратура')
    print(request.GET)

    return render(request, 'edu-programs-catalog.html', context={'programs_bak': programs_bak, 'programs_mag': programs_mag})


def get_edu_bak_cards(request):
    print(request.GET)
    programs = EduProgram.objects.filter(level__contains='Бакалавр')
    #test_program = EduProgram.objects.get(pk=7)
    #test_data = test_program.kafedra_name.institut.name
    #print(test_data)
    #print(type(test_data))
    if len(request.GET.getlist('edu_number')) != 0:
        programs = EduProgram.objects.filter(edu_number__in=request.GET.getlist('edu_number'))
    if len(request.GET.getlist('form')) != 0:
        #forms_dict ={'Очная': 1, 'Заочная': 2, 'Очно-заочная': 3}
        #clear_list = []
        #for form in request.GET.getlist('form'):
        #    clear_list.append(forms_dict[form])
        #programs = programs.filter(eduprogramseduform__edu_form__in=clear_list).distinct()
        #print(clear_list)
        programs = programs.filter(eduprogramseduform__edu_form__name__in=request.GET.getlist('form')).distinct()
    if len(request.GET.getlist('eduBudget')) != 0:
        programs = programs.filter(eduprogramseduform__budget_places__gt=0).distinct()
    if len(request.GET.getlist('eduContract')) != 0:
        programs = programs.filter(eduprogramseduform__contract_places__gt=0).distinct()
    if len(request.GET.getlist('eduPeriod')) != 0:
        programs = programs.filter(eduprogramseduform__lerning_time__in=request.GET.getlist('eduPeriod')).distinct()
    if len(request.GET.getlist('institutName')) != 0:
        programs = programs.filter(kafedra_name__institut__name__in=request.GET.getlist('institutName')).distinct()
    if len(request.GET.getlist('eduFormKafName')) != 0:
        programs = programs.filter(kafedra_name__name__in=request.GET.getlist('eduFormKafName')).distinct()
    #program = EduProgram.objects.filter(eduprogramseduform__edu_form__in=[2,3])
    #program = EduProgram.objects.filter(eduprogramseduform__budget_places__gt=0)
    #program = EduProgram.objects.filter(eduprogramseduform__contract_places__gt=0)
    #program = EduProgram.objects.filter(edu_number__in=[7,8])
    #program = EduProgram.objects.filter(kafedra_name_institut__in=[7,8])
    #program = EduProgram.objects.filter(kafedra_name_in=[7,8])
    #program = program.filter(eduprogramseduform__lerning_time__in=['2 года 6 месяцев'])
    print(len(programs))
    print(type(programs))
    #forms = EduProgram.objects.filter(id=17).get_forms()
    #forms = EduProgramEduForm.objects.filter(edu_form = 1).select_related('edu_program')
    #print((EduProgram.objects.get(id=7).get_forms).__dict__)
    #forms = forms.filter(edu_program_id__in=a)
    #programs = EduProgram.objects.filter(edu_number__in=a,)

    return render(request, 'program_cards.html', context={'programs': programs})


def get_edu_mag_cards(request):
    programs = EduProgram.objects.filter(level__contains='Магистратура')
    if len(request.GET.getlist('edu_number')) != 0:
        programs = EduProgram.objects.filter(edu_number__in=request.GET.getlist('edu_number'))
    if len(request.GET.getlist('form')) != 0:
        programs = programs.filter(eduprogramseduform__edu_form__name__in=request.GET.getlist('form')).distinct()
    if len(request.GET.getlist('eduBudget')) != 0:
        programs = programs.filter(eduprogramseduform__budget_places__gt=0).distinct()
    if len(request.GET.getlist('eduContract')) != 0:
        programs = programs.filter(eduprogramseduform__contract_places__gt=0).distinct()
    if len(request.GET.getlist('eduPeriod')) != 0:
        programs = programs.filter(eduprogramseduform__lerning_time__in=request.GET.getlist('eduPeriod')).distinct()
    if len(request.GET.getlist('institutName')) != 0:
        programs = programs.filter(kafedra_name__institut__name__in=request.GET.getlist('institutName')).distinct()
    if len(request.GET.getlist('eduFormKafName')) != 0:
        programs = programs.filter(kafedra_name__name__in=request.GET.getlist('eduFormKafName')).distinct()
    return render(request, 'program_cards.html', context={'programs': programs})


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


def searching_bak(request):
    programs = EduProgram.objects.filter(level__contains='Бакалавриат').filter(name__contains=request.GET.get('searching'))
    return render(request, 'program_cards.html', context={'programs': programs})

def searching_mag(request):
    programs = EduProgram.objects.filter(level__contains='Магистратура').filter(name__contains=request.GET.get('searching'))
    return render(request, 'program_cards.html', context={'programs': programs})