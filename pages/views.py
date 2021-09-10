from .models import Post, BlogPost
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy


# Create your views here.

# function based view example

# def homePageView(request):
#     return HttpResponse('Hello World')

# class based template view example

# class HomePageView(TemplateView):
#     template_name = 'home.html'


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog')
