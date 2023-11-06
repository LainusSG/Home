from django.shortcuts import render

def index(request):
    return render(request, 'render/index.html', {})

def index2(request):
    return render(request, 'render/index2.html', {})