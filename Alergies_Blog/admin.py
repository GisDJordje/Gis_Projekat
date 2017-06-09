from django.contrib import admin
from .models import Post,Comments 

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','date_created','status','image') 
    list_filter = ('title','author','status')
    search_fields = ('title','author__first_name','status')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
   
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','created') 
    list_filter = ('email','created','active')
    search_fields = ('email','name')
    
admin.site.register(Post,PostAdmin)
admin.site.register(Comments,CommentAdmin)
