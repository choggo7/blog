from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import post

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def post_id(request,idp):
    if idp != None and int(idp) > 0:
        pst = post.objects.filter(id = idp)
        if pst != None:
            return render(request,'blog/post.html',{'pst':pst})
    else:
        return render(request,'blog/404.html')


def post_all(request):
    pst = post.objects.all()
    return render(request,'blog/posts.html',{'pst':pst})

def page_404(request):
    return render(request,'blog/404.html')

def tst(request):
    return render(request,'blog/For Blog Post Article.html')