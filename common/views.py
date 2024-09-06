from django.shortcuts import render

from rest_framework import generics, response
from common.models import Region, District, Social
from common.serializer import RegionListSerializer, DistrictSerializer, SocialSerializer
from rest_framework.views import APIView
class RegionListAPIView(generics.ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all()


class DistrictListByRegionAPIView(generics.ListAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

    def get_queryset(self):
        region_id = self.request.parser_context['kwargs'].get("pk", None)
        qs = super().get_queryset()
        return qs.filter(region_id=region_id)



class SocialListAPIView(generics.ListAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()



class GenderChoicesListAPIView(APIView):

    def get(selfself, request, *args, **kwargs):
        data = [
            {
                "key": "male",
                "value": "Erkak"
            },
            {
                "key": "female",
                "value": "Ayol"
            } ]
        return response.Response(data, status=200)