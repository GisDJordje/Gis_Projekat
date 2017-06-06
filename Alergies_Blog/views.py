from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.core.urlresolvers import reverse
from . models import Post
from . forms import EmailPostForm,CommentForm
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

#Home Page App Template View 
class Home_Page_View(TemplateView):
    template_name = 'Alergies_Blog/home_page.html'
  
  
# Create your views here.
def home_page(request):
     posts = Post.objects.all()
     return render(request, 'Alergies_Blog/home_page_all_posts.html',{'posts':posts}) 

#View with details for specific post
def post_details(request,year,month,day,post):
    post = get_object_or_404(Post,slug= post,
                                    status='published',
                                    publish__year = year,
                                    publish__month = month,
                                    publish__day = day,
                                    ) 
    
    comments = post.comments.filter(active = True) 
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('Alergies:Blog:home_page'))
        else:
            '''return HttpResponse('There was a problem',form)'''
            return render(request,'Alergies_Blog/post_details.html',{'post':post,'form':form,'comments':comments})
    else:
        form = CommentForm()
        return render(request,'Alergies_Blog/post_details.html',{'post':post,'comments':comments,'form':form})

#Sharing posts by email
def post_share(request,pk):
    post = get_object_or_404(Post, id=pk, status ='published')
    
    if request.POST:
        form = EmailPostForm(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['name'],cd['comments'],cd['email'],cd['to'])
        else:
             return render(request,'Alergies_Blog/share_post_form.html',{'form':form})
        
    else:
        form = EmailPostForm()
        
        return render(request,'Alergies_Blog/share_post_form.html',{'form':form,'post':post})
