from django.shortcuts import render

def main(requests):
    return render(requests, 'main.html')

def index(requests):
    return render(requests, 'posts/index.html')
