from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

#Home Page App Template View 
class Home_Page_View(TemplateView):
    template_name = 'Base_templateI.html'
    
# Create your views here.
def home_page(request):
    return render(request, 'Alergies_Blog/Base_template.html') 
