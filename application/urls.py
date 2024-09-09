from django.urls import path
from .views import ApplicationCreateAPIView, AplicationStatusesListAPIView

urlpatterns = [
    path("application-create/", ApplicationCreateAPIView.as_view()),
    path("detail/", AplicationStatusesListAPIView.as_view()),

]