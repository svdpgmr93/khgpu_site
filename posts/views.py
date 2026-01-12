from django.shortcuts import render
from django.http import HttpResponseNotFound

def pageNotFoun(request, exception):
    return HttpResponseNotFound(request,'404.html')

def main(requests):
    return render(requests, 'main.html')

def index(requests):
    return render(requests, 'posts/index.html')

def sveden(requests):
    return render(requests, 'sveden.html')

def common(requests):
    return render(requests, 'common.html') #Основные сведения

def struct(requests):
    return render(requests, 'struct.html') #Структура и органы управления образовательной организацией

def document(requests):
    return render(requests, 'documents.html') #Документы

def education(requests):
    return render(requests, 'education.html') #Образование

def mag_opop(requests):
    return render(requests, 'mag_opop.html')

def bak_opop(requests):
    return render(requests, 'bak_opop.html')

def eduStandarts(requests):
    return render(requests, 'eduStandarts.html') #Образовательные стандарты и требования

def managers(requests):
    return render(requests, 'managers.html') #Руководство

def employees(requests):
    # if HttpResponseNotFound:
    #     return render(requests,'404.html')     # Рабочая тема!
    return render(requests, 'employees.html') #Педагогический состав

def objects(requests):
    return render(requests, 'objects.html') #Материально-техническое обеспечение и

def grants(requests):
    return render(requests, 'grants.html') #Стипендии и меры 

def paid_edu(requests):
    return render(requests, 'paid-edu.html') #Платные образовательные услуги

def budget(requests):
    return render(requests, 'budget.html') #Финансово-хозяйственная деятельность

def vacant(requests):
    return render(requests, 'vacant.html') #Вакантные места для приема (перевода)

def inter(requests):
    return render(requests, 'inter.html') #Международное сотрудничество

def catering(requests):
    return render(requests, 'catering.html') #Организация питания

def career(requests):
    return render(requests, 'career.html')

def media(requests):
    return render(requests, 'templates_media/media.html')

def universitet_v_smi(requests):
    return render(requests, 'templates_media/universitet_v_smi.html')

def anti_corruption(requests):
    return render(requests, 'anti-corruption.html')

def rabota_v_hgpu(requests):
    return render(requests, 'rabota-v-hgpu.html')

def test(requests):
    return render(requests, 'test.html')

def gup(requests):
    return render(requests, 'gup.html') #График учебного процесса