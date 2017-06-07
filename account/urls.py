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
    
   #Url for Home Page            www.hostname.com/account/
    url(r'^$', views.home_page, name = 'home_page'),
    
    #Login Url                        www.hostname.com/account/login
    url(r'^login/$','django.contrib.auth.views.login', name = 'login'),
    
    #Logout Url                        www.hostname.com/account/logout
    url(r'^logout/$','django.contrib.auth.views.logout', name = 'logout'),
    
    #Logout-then-Login Url                        www.hostname.com/account/logout
    url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login', name = 'logout'),
    
    #Sign Up URL                        www.hostname.com/accounts/signup
    url(r'^sign_up/$',views.sign_up, name = 'sign_up'),
    
]