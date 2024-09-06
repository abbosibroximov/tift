from django.urls import path
from news.views import NewsContentListAPIView, NewsContentDetailAPIView

urlpatterns = [
    path("news/", NewsContentListAPIView.as_view()),
    path("news/<str:slug>/", NewsContentDetailAPIView.as_view()),

]