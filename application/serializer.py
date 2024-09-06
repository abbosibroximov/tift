from rest_framework import serializers
from .models import Application
from education.serializer import DirectionModelSerializer
from common.serializer import DistrictSerializer
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("first_name", "last_name", "passport", "pinfl", "gender", "birth_date",
                  "direction", "district")

        def create(self, validated_data):
            user = self.context['request'].user
            validated_data['user_id'] = user.id
            return super().create(validated_data)


class ApplicationDetailSerializer(serializers.ModelSerializer):
    direction = DirectionModelSerializer
    district = DistrictSerializer
    status = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    class Meta:
        model = Application
        fields = ("first_name", "last_name", "passport", "pinfl", "gender", "birth_date",
                  "direction","status", "district", "accepted_at", "created")

    def get_status(self, obj):
        return obj.get_status_display()

    def get_gender(self, obj):
        return obj.get_gender_display()
