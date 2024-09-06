from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializer import ApplicationSerializer , ApplicationDetailSerializer
from .models import Application
from rest_framework.permissions import IsAuthenticated
class ApplicationCreateAPIView(CreateAPIView):
    queryset = Application
    serializer_class = ApplicationSerializer

    permission_classes = (IsAuthenticated, )


class AplicationStatusesListAPIView(ListAPIView):
    serializer_class = ApplicationDetailSerializer
    queryset = Application.objects.all()
    permission_classes = (IsAuthenticated, )


    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)