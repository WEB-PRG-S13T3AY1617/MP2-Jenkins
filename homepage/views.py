#from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from django.http import Http404
from .models import Post, User


def index(request):
    try:
        request.session["username"]
        all_posts = Post.objects.all()
        context = {'all_posts': all_posts}
        return render(request, 'homepage/index.html', {'all_posts': all_posts})
    except :
        request.session["username"] = " "
        all_posts = Post.objects.all()
        context = {'all_posts': all_posts}
        return render(request, 'homepage/index.html', {'all_posts': all_posts})


def search(request):

        request.session["search"]=request.POST['search']
        all_posts = Post.objects.all()
        context = {'all_posts': all_posts}

        return render(request, 'homepage/search.html', {'all_posts': all_posts})



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


def submit(request):

    newuser=User()
    newuser.name=request.POST['name']
    newuser.username=request.POST['username']
    newuser.password=request.POST['password']
    newuser.dpo=request.POST['dpo']
    newuser.save()

    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}

    return render(request, 'homepage/index.html', {'all_posts': all_posts})

    #return HttpResponse("USER ADDED CHECK ADMIN")
    
def login(request):
    
    
    return render(request, 'homepage/login.html')

def lsubmit(request):
    
    tempuser = User()
    uname=request.POST['username']
    passw=request.POST['password']



    try:
             tempuser = User.objects.get(username = request.POST['username'])
        
    except User.DoesNotExist:

             return render(request, 'homepage/login.html')

    if tempuser.password!=passw:
            return render(request, 'homepage/login.html')

    request.session["username"] = uname

    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}

    return render(request, 'homepage/index.html', {'all_posts': all_posts})

    #return HttpResponse('LOGIN Success! Hello ' + request.session["username"] + '!!!')


        





def postnew(request):
    
    return render(request, 'homepage/addpost.html')

def psubmit(request):
    try:
        tempuser = User.objects.get(username=request.session['username'])
        newpost = Post()
        newpost.ownername = tempuser
        newpost.itemname = request.POST['itemname']
        #newpost.thumbnail = request.POST['thumbnail']
        newpost.quantity = request.POST['quantity']
        newpost.condition = request.POST['condition']
        newpost.itemtype = request.POST['itemtype']
        newpost.tags = request.POST['tags']

        newpost.save()
        all_posts = Post.objects.all()
        context = {'all_posts': all_posts}
        return render(request, 'homepage/index.html', {'all_posts': all_posts})
    except :
        return render(request, 'homepage/addpost.html')

def logout(request):
    del request.session['username']
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'homepage/index.html', {'all_posts': all_posts})