from django.urls import path
from .views import (HomePageView, AboutPageView, BlogListView,
                    BlogPostDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView)

urlpatterns = [
    # url for function based view
    # path('', homePageView, name="home"),
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('blog/', BlogListView.as_view(), name="blog"),
    path('blog/new/', BlogCreateView.as_view(), name="post_new"),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name="post_edit"),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name="post_delete"),
]
