'''
Created on 06.06.2017.

@author: Asus
'''

from django import forms
from .models import Comments
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