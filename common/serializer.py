from rest_framework import serializers
from common.models import Region, District, Social, GenderChoices

class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "title"]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "title"]


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ["id", "title", "social", "link"]
