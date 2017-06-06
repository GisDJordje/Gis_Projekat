from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone 
from django.contrib.auth.models import User 

# Create your models here.
# Create Manager 
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

#Creating Post Model 
class Post(models.Model):
    
    STATUS_CHOICES = (
        
        ('draft','Draft'),
        ('published','Published')
    )
    
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique_for_date='publish')
    body = models.TextField() 
    publish = models.DateTimeField(default = timezone.now())
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True) 
    author = models.ForeignKey(User,on_delete = models.CASCADE,related_name='blog_posts') 
    status = models.CharField(max_length = 20,choices=STATUS_CHOICES,default='draft') 
    objects = models.Manager() 
    published = PublishedManager()
    
    
    
    class Meta:
        ordering = ('-date_created',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('myblog:post_details',args=[self.publish.year,
                                                   self.publish.strftime('%m'),
                                                   self.publish.strftime('%d'),
                                                   self.slug]) 
        
class Comments(models.Model):
    post = models.ForeignKey(Post,related_name="comments") 
    name = models.CharField(max_length = 100)
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add = True) 
    updated = models.DateTimeField(auto_now = True) 
    active = models.BooleanField(default=True) 
    
    def __str__(self):
        return "Commented by {} on {}".format(self.name,self.post)
    
    class Meta:
        ordering = ('-created',) 
        
        
        
        