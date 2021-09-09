from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Post, BlogPost

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
