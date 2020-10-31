from django.test import Client, TestCase


class TestViews(TestCase):
    def test_homepage_status(self):
        client = Client()
        response = client.get('/nopage')
        self.assertEqual(response.status_code, 404)
