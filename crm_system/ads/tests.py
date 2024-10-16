from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group

from decimal import Decimal
from .models import Ads
from customers.models import Customer
from leads.models import Lead
from products.models import Product


class TestAppAds(TestCase):
    fixtures = ['backup.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_marketer: User = User.objects.create_user(
            username='marketer',
            password='qwerty123@'
        )
        cls.test_product = Product.objects.create(
            name='test_product',
            description='test_description',
            cost=Decimal('2999.99'),
            created_by=cls.test_marketer,
        )
        cls.test_ad = Ads.objects.create(
            name='test_ad',
            product=cls.test_product,
            channel='test_channel',
            budget=29990,
        )
        cls.test_marketer.groups.add(Group.objects.get(name='Marketer'))

    @classmethod
    def tearDownClass(cls):
        cls.test_marketer.delete()
        cls.test_product.delete()
        cls.test_ad.delete()

    def setUp(self):
        self.client.force_login(self.test_marketer)

    def tearDown(self):
        self.client.logout()

    def test_list_view(self):
        response = self.client.get(reverse('ads:ads'))
        self.assertEqual(response.status_code, 200)
        for i_ads in Ads.objects.all():
            with self.subTest(f'Test for the presence ad: {i_ads.name}'):
                self.assertContains(response, i_ads.name, html=True)

    def test_statistic_view(self):
        response = self.client.get(reverse('ads:ads_statistic'))
        self.assertEqual(response.status_code, 200)
        for ad in Ads.objects.all():
            sum_cost_contracts = 0
            for customer in Customer.objects.filter(ad=ad.pk):
                sum_cost_contracts += customer.contract.cost
            count_leads = Lead.objects.filter(ad=ad.pk).count()
            count_customers = Customer.objects.filter(ad=ad.pk).count()
            with self.subTest('Test for the presence of advertising statistics'):
                self.assertContains(response, ad.name, html=True)
                self.assertContains(response, count_leads)
                self.assertContains(response, count_customers)

    def test_create_ad_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(reverse('ads:ad_create'))
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            form_data = {
                'name': 'new_ad',
                'product': f'{self.test_product.pk}',
                'channel': 'someone_channel',
                'budget': 15000,
            }
            response_with_data = self.client.post(
                reverse('ads:ad_create'),
                data=form_data,
                follow=True
            )
            self.assertEqual(response_with_data.status_code, 200)
            self.assertTrue(Ads.objects.filter(name=form_data['name']).exists())

    def test_detail_ad_view(self):
        response = self.client.get(
            reverse(
                'ads:ad_detail',
                kwargs={'pk': self.test_ad.pk}
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_update_ad_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'ads:ad_update',
                    kwargs={'pk': self.test_ad.pk}
                )
            )
            self.assertEqual(response.status_code, 200)
        with self.subTest('Test post method'):
            form_data = {
                'name': 'new_ad',
                'product': f'{self.test_product.pk}',
                'channel': 'new_channel',
                'budget': 15000,
            }
            response_with_data = self.client.post(
                reverse('ads:ad_update', kwargs={'pk': self.test_ad.pk}),
                data=form_data,
                follow=True,
            )
            self.assertEqual(response_with_data.status_code, 200)
            self.assertTrue(Ads.objects.filter(name=form_data['name']).exists())

    def test_delete_ad_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'ads:ad_delete',
                    kwargs={'pk': self.test_ad.pk}
                )
            )
            self.assertEqual(response.status_code, 200)
        with self.subTest('Test post method'):
            new_ad = Ads.objects.create(
                name='test_ad',
                product=self.test_product,
                channel='test_channel',
                budget=29990,
            )
            response = self.client.post(
                reverse(
                    'ads:ad_delete',
                    kwargs={'pk': new_ad.pk}
                )
            )
            self.assertEqual(response.status_code, 302)
