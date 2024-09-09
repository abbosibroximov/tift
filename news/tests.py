from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import NewsContent
from datetime import datetime


class NewsContentAPITestCase(APITestCase):
    def setUp(self):
        self.item_active = NewsContent.objects.create(
            title="test newaskldsaklds",
            body="test news test",
            is_published=True,
            publish_time=datetime(2024, 8, 29, 12, 30, 00),

        )
        self.item_inactive = NewsContent.objects.create(
            title="test news",
            body="test news test",
            is_published=False,
            publish_time=datetime(2024, 9, 11, 12, 30, 00),

        )
        self.list_url = reverse('news-list')

    def test_news_content_list_api(self):
        response = self.client.get(self.list_url)
        r = response.json()
        count = r.get('count')
        data = r.get('results')[0]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, count)
        self.assertEqual(self.item_active.title, data['title'])
        self.assertEqual(self.item_active.slug, data['slug'])


__all__ = ["NewsContentAPITestCase"]
