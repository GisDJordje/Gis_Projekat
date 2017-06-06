'''
Created on 06.06.2017.

@author: Asus
'''

'''
Created on 30.03.2017.

@author: Asus
'''
from django.conf.urls import url
from .import views

urlpatterns = [
    
   #Url for Home Page            www.hostname.com/blog/
    url(r'^$', views.home_page, name = 'home_page'),
    
    
    
    
]