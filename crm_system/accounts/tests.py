from django.test import TestCase

from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from ads.models import Ads
from leads.models import Lead
from customers.models import Customer


class TestAppAccounts(TestCase):
    fixtures = ['backup.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_user: User = User.objects.create_user(
            username='user',
            password='qwerty123@'
        )

    @classmethod
    def tearDownClass(cls):
        cls.test_user.delete()

    def setUp(self):
        self.client.force_login(self.test_user)

    def tearDown(self):
        self.client.logout()

    def test_index(self):
        response = self.client.get(reverse('accounts:account_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, Product.objects.count())
        self.assertContains(response, Ads.objects.count())
        self.assertContains(response, Lead.objects.count())
        self.assertContains(response, Customer.objects.count())

    def test_redirect_login(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertRedirects(response, reverse('accounts:account_index'))

    def test_redirect_logout(self):
        response = self.client.post(reverse('accounts:logout'))
        self.assertRedirects(response, reverse('accounts:login'))
