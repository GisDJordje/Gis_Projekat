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
    
    #Url for details about specific post        www.hostname.com/blog/2017/05/20/2
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_details,name='post_details'),
    
    #url(r'^share_post/(?P<pk>\d{1,2})/$', views.post_share,name='post_share'),
     
]

 








