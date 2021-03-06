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
from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings 
from django.conf.urls.static import static


from .views import Home_Page_View
from Alergies_Blog.views import Home_Page_View

urlpatterns = [
    #localhost:        #Admin Page
    url(r'^admin/', admin.site.urls), 
    #Home Page                   #http://127.0.0.1:8000/
    url(r'^$',Home_Page_View.as_view(), name = "home_page"),
    #Alergies Blog                  #http://127.0.0.1:8000/alergies_blog
    url(r'^alergies_blog/',include('Alergies_Blog.urls', namespace = "alergies_blog")),
    
     #Account app                  #http://127.0.0.1:8000/account
    url(r'^account/',include('account.urls', namespace = "account")),
    #Alergies maper app                  #http://127.0.0.1:8000/alergies_maper
    url(r'^alergies_maper/',include('alergies_maper.urls', namespace = "alergies_maper")),
   
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
