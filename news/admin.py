from django.contrib import admin

from news import models

@admin.register(models.NewsContent)
class NewsContentAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "is_published", "publish_time"]
    list_editable = ["is_published", "publish_time"]
    exclude = ["slug"]
    list_filter = ["is_published",]
    search_fields = ["title", "body"]