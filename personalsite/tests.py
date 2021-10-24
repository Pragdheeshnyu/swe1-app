from django.test import TestCase


class QuestionIndexViewTests(TestCase):
    def test_html_admin(self):
        response = self.client.get("/admin")
        self.assertEqual(response.status_code, 301)
