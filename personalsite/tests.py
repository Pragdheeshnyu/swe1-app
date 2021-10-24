from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse


class QuestionIndexViewTests(TestCase):
    def test_html_admin(self):
        response = self.client.get("/admin")
        self.assertEqual(response.status_code, 301)

    # def test_html_
