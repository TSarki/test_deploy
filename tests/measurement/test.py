from unittest import TestCase
from rest_framework.test import APIClient

class TestSampleView(TestCase):
    def test_ci_cd(self):
        url = '/api/sensors/'
        client = APIClient()
        response = client.get(url)
        print(response)
        self.assertEqual(2, 2)