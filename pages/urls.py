from django.urls import path
from .views import HomePageView, AboutPageView, BlogListView, BlogPostDetailView

urlpatterns = [
    # url for function based view
    # path('', homePageView, name="home"),
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('blog/', BlogListView.as_view(), name="blog"),
]
