from unittest import TestCase
from rest_framework.test import APIClient

class TestSampleView(TestCase):
    def test_view(self):
        url = '/api/sensors/'
        client = APIClient()
        response = client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)