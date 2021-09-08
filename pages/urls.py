from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # url for function based view
    # path('', homePageView, name="home"),
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
]
