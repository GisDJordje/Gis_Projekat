from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.core.urlresolvers import reverse
from . models import Post
from . forms import EmailPostForm,CommentForm,CreatePostForm
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

#Home Page App Template View 
class Home_Page_View(TemplateView):
    template_name = 'Alergies_Blog/home_page.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['isRegistred'] = self.request.user.is_authenticated()
        ctx['section'] = 'Home'
        return ctx
  
  
# Blog Home Page View With All Posts
def home_page(request):
     posts = Post.objects.all()
     return render(request, 'Alergies_Blog/home_page_all_posts.html',{'posts':posts,'section':'blog'}) 

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
            return HttpResponseRedirect(reverse('alergies_blog:home_page'))
        else:
            '''return HttpResponse('There was a problem',form)'''
            return render(request,'Alergies_Blog/post_details.html',{'post':post,'form':form,'comments':comments})
    else:
        form = CommentForm()
        return render(request,'Alergies_Blog/post_details.html',{'post':post,'comments':comments,'form':form})


#View Form Update
def update_post(request,pk):
    post = get_object_or_404(Post,pk=pk) 
    if request.POST:
        post = CreatePostForm(request.POST, instance = post)
        if post.is_valid():
            post.save() 
            return HttpResponseRedirect(reverse("alergies_blog:home_page"));
        else:
            return render(request,'Alergies_Blog/update_post.html',{'form':post})
    else:
        form = CreatePostForm(instance = post)
        return render(request,'Alergies_Blog/update_post.html',{'form':form})

def create_post(request):
    if request.POST:
        form = CreatePostForm(request.POST, request.FILES) 
        if form.is_valid():
            post = form.save() 
            return HttpResponse("You Saved Your Form")
        else:
             return render(request,'Alergies_Blog/create_post.html',{'form':form})
    else:
        form = CreatePostForm()
        return render(request,'Alergies_Blog/create_post.html',{'form':form})




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


def delete_post(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.delete()
    return HttpResponse("Post is deleted")





    
