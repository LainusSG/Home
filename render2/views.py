from django.shortcuts import render

def index(request):
    return render(request, 'render2/index.html', {})
