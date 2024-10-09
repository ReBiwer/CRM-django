from django.test import TestCase

from django.urls import reverse
from django.contrib.auth.models import User, Group
from products.models import Product
from ads.models import Ads
from leads.models import Lead
from customers.models import Customer


class TestAppAccounts(TestCase):
    fixtures = ['backup.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_operator: User = User.objects.create_user(
            username='operator',
            password='qwerty123@'
        )
        cls.test_operator.groups.add(Group.objects.get(name='Operator'))

    @classmethod
    def tearDownClass(cls):
        cls.test_operator.delete()

    def setUp(self):
        self.client.force_login(self.test_operator)

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
