'''
Created on 06.06.2017.

@author: Asus
'''

from django import forms
from .models import Comments
from .models import Post
from django.forms.widgets import Textarea


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField() 
    to = forms.CharField(max_length = 100)
    comments = forms.CharField(widget = forms.Textarea,required = False) 
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments 
        fields = ('name','email','body') 
        
class CreatePostForm(forms.ModelForm):
    
    def __init__(self,*args, **kwargs):
        super(CreatePostForm,self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get('field_name')
            if field:
                field.widget.attrs.update({'placeholder':field.label,'class':'form-control'})
        
         
    class Meta:
        model = Post
        exclude = ('objects',)
        
        
        
        
        