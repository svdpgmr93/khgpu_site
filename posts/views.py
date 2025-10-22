from django.shortcuts import render
from django.http import HttpResponseNotFound

def pageNotFoun(request, exception):
    return HttpResponseNotFound(request,'404.html')

def main(requests):
    return render(requests, 'main.html')

def index(requests):
    return render(requests, 'posts/index.html')

def education_organization(requests):
    return render(requests, 'posts/education-organization.html')

def basic_info(requests):
    return render(requests, 'posts/basic-info.html')

def documents(requests):
    return render(requests, 'documents.html')

def paid_edu(requests):
    return render(requests, 'paid-edu.html')