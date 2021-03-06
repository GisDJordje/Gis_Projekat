from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView,View
import json

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'alergies_maper/dashboard.html' 
        
    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['section'] = 'workspace'
        return ctx 

def get_all_patientes(request):
    import psycopg2
    conn_postgres = psycopg2.connect("dbname=PyAlergies user=postgres password=coperman") 
    cur_postgres = conn_postgres.cursor() 
    SQL = "SELECT * FROM patiente_postgis" 
    cur_postgres.execute(SQL) 
    data = cur_postgres.fetchall() 
    data = data
    section = 'People'
    names = ("id","ime","prezime","dijagnoze","pol","vreme_rodjenja","adresa","latlon","filijala","ispostava",
                "kijanje","sekrecija","zapusen_nos","kasalj","gusenje","sviranje","rhinitis_chr","rhinitis_na","rhinitis_a","astma",
                "konjuktivitis"
            )
    """cur_postgres.execute("SELECT column_name FROM information_schema.columns WHERE table_name= 'patiente_postgis'") 
    col_names = cur_postgres.fetchall() """
    return render(request,"alergies_maper/all_patientes.html",{'data':data,"names":names,'section':section})

def get_workspace(request):
    import requests
    url = 'http://localhost:8090/geoserver/rest/workspaces' 
    auth = ('admin','geoserver') 
    headers = {'Content-Type':'application/json','Accept':'application/json'} 
    r = requests.get(url = url,headers = headers, auth = auth)
    return HttpResponse(r,content_type="application/json")
    
def get_layers(request):
    import requests
    url = 'http://localhost:8090/geoserver/rest/layers' 
    auth = ('admin','geoserver') 
    headers = {'Content-Type':'application/json','Accept':'application/json'} 
    r = requests.get(url = url,headers = headers, auth = auth)
    return HttpResponse(r,content_type="application/json")




def getws(request):
    return render(request, 'alergies_maper/rest.html') 

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'alergies_maper/charts.html')
    
def get_data(request):
    return JsonResponse({"Ime":"Djordje","Prezime":"Subotic","Godine":27})    
    
    
    
    
    
    
    
