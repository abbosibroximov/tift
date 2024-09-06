from django.urls import path
from common.views import RegionListAPIView, DistrictListByRegionAPIView, SocialListAPIView,  GenderChoicesListAPIView

urlpatterns = [
    path("region/", RegionListAPIView.as_view()),
    path("<int:pk>/district/", DistrictListByRegionAPIView.as_view()),
    path("social/", SocialListAPIView.as_view()),
    path("genders/", GenderChoicesListAPIView.as_view()),

]