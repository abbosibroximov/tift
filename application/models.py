from django.db import models
from django.contrib.auth import get_user_model
from common.models import District, GenderChoices
from education.models import Direction
from datetime import datetime

User = get_user_model()


class StatusChoices(models.TextChoices):
    Accepted = "accepted", "Qabul qilingan"
    Rejected = "rejected", "Rad etilgan"
    In_process = "in_process", "Jarayonda"


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    passport = models.CharField(max_length=20)
    pinfl = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    birth_date = models.DateField()
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.In_process)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    accepted_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if (self.status == StatusChoices.Accepted or self.status == StatusChoices.Rejected) and not self.accepted_at:
            self.accepted_at = datetime.now()
        return super().save(*args, **kwargs)