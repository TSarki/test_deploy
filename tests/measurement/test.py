from unittest import TestCase
from rest_framework.test import APIClient

class TestSampleView(TestCase):
    def test_ci_cd(self):
        self.assertEqual(2, 2)