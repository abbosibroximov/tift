from django.contrib import admin

from application import models

@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "passport", "status"]
    list_editable = ["status", ]