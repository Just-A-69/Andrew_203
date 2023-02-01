from django.shortcuts import render
from .models import Project

def project_index(request):
    all_posts = Project.objects.all()
    context = {
        'all_posts':all_posts
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    post = Project.objects.get(pk=pk)
    context = {
        'post':post
    }
    return render(request, 'project_detail.html', context)