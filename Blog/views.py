from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Category
# Create your views here.

# def index(request):
#   return render(request,'Blog.html')


def postcategory(request, categorypost):
    Data = {'Categories': Category.objects.all(),
    'Posts': Post.objects.filter(category=categorypost)}
    return render(request, 'Blog.html', Data)


def list(request):
    data = {'Categories': Category.objects.all(),
    		'Posts': Post.objects.all()}
    return render(request, 'Blog.html', data)


def postid(request, category, slugifytitle):
    Data = {'Categories': Category.objects.all(),
    		'POSTID': Post.objects.get(slugifytitle=slugifytitle)}
    return render(request, 'PostId.html', Data)

def about(request):
    Data = {'Categories': Category.objects.all()}
    return render(request, 'about.html', Data)

def contact(request):
    Data = {'Categories': Category.objects.all()}
    return render(request, 'contact.html', Data)

def archive(request):
    Data = {'Categories': Category.objects.all()}
    return render(request, 'archive.html', Data)

