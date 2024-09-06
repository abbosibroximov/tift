from rest_framework import serializers
from news.models import NewsContent
class NewsContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContent
        fields = ("title", "slug", "publish_time")



class NewsContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContent
        fields = ("title", "body", "slug", "publish_time")
