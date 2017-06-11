'''
Created on 06.06.2017.

@author: Asus
'''
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse
#Home Page App Template View 
class Home_Page_View(TemplateView):
    template_name = 'Base_templateI.html'
    
    
def get_workspace(request):
    import requests
    url = 'http://localhost:8090/geoserver/rest/workspaces' 
    auth = ('admin','geoserver') 
    headers = {'Content-Type':'application/json','Accept':'application/json'} 
    r = requests.get(url = url,headers = headers, auth = auth)
    return HttpResponse(r,content_type="application/json")