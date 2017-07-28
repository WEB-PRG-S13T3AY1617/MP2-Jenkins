#from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from django.http import Http404
from .models import Post, User


def index(request):
    all_posts = Post.objects.all()
    context = { 'all_posts': all_posts }

    return render(request, 'homepage/index.html', { 'all_posts': all_posts })

def postdetail(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist.")
    return render(request, 'homepage/postdetails.html', { 'post': post })

def userdetail(request, user_username):
    try:
        user = User.objects.get(username = user_username)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    return render(request, 'homepage/userdetails.html', { 'user': user })


def register(request):


    return render(request,'homepage/register.html')