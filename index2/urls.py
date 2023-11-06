from django.urls import path

from index2 import views

urlpatterns = [
    path('', views.index, name='index'),
]