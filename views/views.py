from django.shortcuts import views

def index(request):
    return views (request, 'render/index.html', {})