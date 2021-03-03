from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse
# posts = [
  # {
    # 'author':'Bhanu dixit',
    # 'title': 'Blog post 1',
    # 'content':'First post content',
    # 'date_posted':'22 feb 2021'
    # },
    # {
    #   'author':'Sageeta dixit',
    #   'title': 'Blog post 2',
    #   'content':'Second post content',
    #   'date_posted':'23 feb 2021'
    # }
# ]

def home(request):
  context = {
    # 'title':'hello',
    'posts':Post.objects.all()
  }
  return render(request,'blog/home.html',context)

def about(request):
  return render(request,'blog/about.html',{'title':'About'})
# Create your views here.
 