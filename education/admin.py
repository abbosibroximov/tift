from django.contrib import admin
from education import models


@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "bio", "phone_number"]


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ["title", "director", "degree"]



@admin.register(models.Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ["title", "language", "faculty", "education_type"]
    list_editable = ["language", "education_type"]