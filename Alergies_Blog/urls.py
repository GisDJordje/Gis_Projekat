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
    
    url(r'^share/(?P<pk>\d{1,2})/$', views.post_share,name='post_share'),
    
    #Url for Create Post          www.hostname.com/blog/
    url(r'^create_post$', views.create_post, name = 'create_post'),
    #Url For Post Updating        www.hostname.com/alergies_blog/2017/05/20/2/update
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/edit/$', views.update_post,name='post_update'),
    #Url for Create Post          www.hostname.com/blog/
    url(r'^update_post/(?P<pk>\d{1,2})/$', views.update_post, name = 'post_update'),
    url(r'^delete_post/(?P<pk>\d{1,2})/$', views.delete_post, name = 'delete_post'),
     
]

 








