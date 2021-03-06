'''
Created on 07.06.2017.

@author: Asus
'''

"""Py_Alergies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #Dashboard View        #Admin Page
    url(r'^$', views.DashboardView.as_view(), name="dashboard"), 
    url(r'^all_patientes$', views.get_all_patientes, name="all_patientes"), 
    url(r'^get_workspace$', views.get_workspace, name="get_workspace"), 
    url(r'^get_layers$', views.get_layers, name="get_layers"), 
    url(r'^get_workspace/my_rest$', views.getws, name="getws"), 
    url(r'^test_charts$', views.HomeView.as_view(), name="get_charts"),
    url(r'^get_data$', views.get_data, name="get_data"), 
 


]
