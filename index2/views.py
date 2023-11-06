from django.shortcuts import render

def index2(request):
    return render(request, 'index2/index.html', {})
