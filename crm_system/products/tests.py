from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group

from .models import Product
from decimal import Decimal


class TestProductApp(TestCase):
    fixtures = ['backup.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_marketer = User.objects.create_user(
            username='marketer',
            password='qwerty123@',
        )
        cls.test_marketer.groups.add(Group.objects.get(name='Marketer'))
        cls.test_product = Product.objects.create(
            name='test_product',
            description='test description',
            cost=Decimal('2999.99'),
            created_by=cls.test_marketer,
        )

    @classmethod
    def tearDownClass(cls):
        cls.test_marketer.delete()

    def setUp(self):
        self.client.force_login(self.test_marketer)

    def tearDown(self):
        self.client.logout()

    def test_list_product_view(self):
        response = self.client.get(reverse('products:products'))
        self.assertEqual(response.status_code, 200)
        for i_product in Product.objects.all():
            with self.subTest(f'Test for presence product: {i_product.name}'):
                self.assertContains(response, i_product.name, html=True)

    def test_create_product_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(reverse('products:products_create'))
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            form_data = {
                'name': 'new_product',
                'description': 'description new product',
                'cost': '5099.99',
            }
            response_with_data = self.client.post(
                reverse('products:products_create'),
                data=form_data,
                follow=True,
            )
            self.assertEqual(response_with_data.status_code, 200)
            self.assertTrue(
                Product.objects.filter(name=form_data['name']).exists()
            )

    def test_detail_product_view(self):
        response = self.client.get(
            reverse(
                'products:products_detail',
                kwargs={'pk': self.test_product.pk},
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_update_product_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'products:products_update',
                    kwargs={'pk': self.test_product.pk}
                )
            )
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            form_data = {
                'name': 'change_product',
                'description': 'description change product',
                'cost': '5100.00',
            }
            response_with_data = self.client.post(
                reverse(
                    'products:products_update',
                    kwargs={'pk': self.test_product.pk}
                ),
                data=form_data,
                follow=True,
            )
            self.assertEqual(response_with_data.status_code, 200)
            self.assertTrue(
                Product.objects.filter(name=form_data['name']).exists()
            )

    def test_delete_product_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'products:products_delete',
                    kwargs={'pk': self.test_product.pk},
                )
            )
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            check_pk_product = self.test_product.pk
            response = self.client.post(
                reverse(
                    'products:products_delete',
                    kwargs={'pk': self.test_product.pk},
                )
            )
            self.assertEqual(response.status_code, 302)
            self.assertFalse(Product.objects.filter(pk=check_pk_product).exists())
