from django.shortcuts import render
from .models import Comment, Post
from .forms import CommentForm
from django.http import HttpResponseRedirect

def comments_index(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts':all_posts
    }
    return render(request, 'comments_index.html', context)

def comments_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            my_comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            my_comment.save()
            return HttpResponseRedirect(f'/comments/{pk}')
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'comments_detail.html', context)

def comments_cat(request, name):
    posts = Post.objects.filter(categories__name=name).order_by('-created_on')
    context = {
        'category':name,
        'posts':posts
    }
    return render(request, 'comments_category.html', context)
