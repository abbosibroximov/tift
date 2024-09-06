from django.shortcuts import render
from .serializer import NewsContentListSerializer, NewsContentDetailSerializer
from .models import NewsContent
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.utils import timezone

class NewsContentListAPIView(ListAPIView):
    queryset = NewsContent.objects.filter(is_published=True, publish_time__lte=timezone.now()).order_by('id')
    serializer_class = NewsContentListSerializer


class NewsContentDetailAPIView(RetrieveAPIView):
    queryset = NewsContent.objects.filter(is_published=True, publish_time__lte=timezone.now()).order_by('id')
    serializer_class = NewsContentDetailSerializer
    lookup_field = "slug"