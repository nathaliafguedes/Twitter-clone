from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.forms.fields import ImageField
from django import forms

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES)

        #If the form is valid
        if form.is_valid():
            #yes, save
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')


            
        else:
            #no, show error
            return HttpResponseRedirect(form.errors.as_json())




    #Get all posts,, limit = 20
    posts = Post.objects.all()[:20]

    # show
    return render(request, 'posts.html',
                 {'posts': posts})

def delete(request, post_id):
    #Find user
    
    post= Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post=Post.objects.get(id=post_id)
        
    if request.method == "POST":
        form =PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect("NotVALID")

    return render(request, 'edit.html',
                  {'post': post})

def LikeView(request,post_id):
    like = Post.objects.get(id=post_id)
    like.likes +=1
    like.save()
    return HttpResponseRedirect('/')
