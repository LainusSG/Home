from django.http import HttpResponse   
from django.template.loader import get_template

class HomeView2():
    def home (self):
        plantilla = get_template('index2.html')
        return HttpResponse (plantilla.render()) 

