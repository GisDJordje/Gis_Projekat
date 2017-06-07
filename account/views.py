from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from .forms import UserRegistrationForm
# Create your views here.
def home_page(request):
    return render(request,'account/Base_template.html') 


#Sign Up View 
def sign_up(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register1.html',{'form': user_form}) 
