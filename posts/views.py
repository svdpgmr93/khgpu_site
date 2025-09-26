from django.shortcuts import render

def main(requests):
    return render(requests, 'base.html')

def index(requests):
    return render(requests, 'posts/index.html')
