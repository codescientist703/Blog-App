from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import AddPost


def home(request):
    allPosts = Post.objects.all()
    context = {
        'posts': allPosts
    }
    return render(request, 'home.html', context)


def dashboard(request):
    allPosts = Post.objects.all()
    context = {
        'posts': allPosts
    }
    return render(request, 'dashboard.html', context)


def add_post(request):
    if not request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddPost()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)


def edit_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = AddPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddPost(instance=post)

    return render(request, 'add_post.html', {'form': form})


def delete_post(request, id):
    if request.method == 'POST':
        post = Post.objects.get(pk=id)
        post.delete()
        return redirect('dashboard')
