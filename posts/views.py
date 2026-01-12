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
    return render(requests, 'common.html')

def struct(requests):
    return render(requests, 'struct.html')

def document(requests):
    return render(requests, 'documents.html')

def education(requests):
    return render(requests, 'education.html')

def mag_opop(requests):
    return render(requests, 'mag_opop.html')

def bak_opop(requests):
    return render(requests, 'bak_opop.html')

def eduStandarts(requests):
    return render(requests, 'eduStandarts.html')

def managers(requests):
    return render(requests, 'managers.html')

def employees(requests):
    # if HttpResponseNotFound:
    #     return render(requests,'404.html')     # Рабочая тема!
    return render(requests, 'employees.html')

def objects(requests):
    return render(requests, 'objects.html')

def grants(requests):
    return render(requests, 'grants.html')

def paid_edu(requests):
    return render(requests, 'paid-edu.html')

def budget(requests):
    return render(requests, 'budget.html')

def vacant(requests):
    return render(requests, 'vacant.html')

def inter(requests):
    return render(requests, 'inter.html')

def catering(requests):
    return render(requests, 'catering.html')

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