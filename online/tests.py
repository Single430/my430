from django.test import TestCase
from django.core.urlresolvers import reverse

from online.models import User


class StatusTest(TestCase):
    def test_login_status(self):
        """
        Test
        """
        response = self.client.get(reverse('online:login'))
        self.assertEqual(response.status_code, 200)

    def test_account_status(self):
        """
        Test
        """
        response = self.client.get(reverse('online:account'))
        self.assertEqual(response.status_code, 200)