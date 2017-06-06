'''
Created on 06.06.2017.

@author: Asus
'''
from django.views.generic.base import TemplateView

#Home Page App Template View 
class Home_Page_View(TemplateView):
    template_name = 'Base_templateI.html'
    