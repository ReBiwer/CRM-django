from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Customer
from contracts.models import Contract
from ads.models import Ads
from leads.models import Lead
from products.models import Product
from decimal import Decimal
from datetime import date


class TestAppCustomers(TestCase):
    fixtures = ['backup.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_manager = User.objects.create_user(
            username='manager',
            password='qwerty123@',
        )
        cls.test_manager.groups.add(Group.objects.get(name='Manager'))
        cls.test_file = SimpleUploadedFile(
            name='test_file.txt',
            content=b'This if a test file',
            content_type='text/plain'
        )
        cls.test_contract = Contract.objects.create(
            name='test_contract',
            product=Product.objects.first(),
            document=cls.test_file,
            description='description for test contract',
            cost=Decimal('12000.00'),
            start_date=date(day=14, month=10, year=2024),
            end_date=date(day=14, month=10, year=2025),
        )
        cls.test_customer = Customer.objects.create(
            first_name='test_f_name',
            surname='test_s_name',
            last_name='test_l_name',
            email='test@mail.ru',
            phone='89091260929',
            ad=Ads.objects.first(),
            contract=cls.test_contract,
        )

    @classmethod
    def tearDownClass(cls):
        cls.test_manager.delete()
        cls.test_contract.delete()

    def setUp(self):
        self.client.force_login(self.test_manager)

    def tearDown(self):
        self.client.logout()

    def test_list_customers_view(self):
        response = self.client.get(reverse('customers:customers'))
        self.assertEqual(response.status_code, 200)
        for i_customer in Customer.objects.all():
            with self.subTest(f'Test for presence customer: {i_customer.first_name}'):
                self.assertContains(response, f'{i_customer.last_name} {i_customer.first_name}', html=True)

    def test_create_customer_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(reverse('customers:customer_create'))
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            contract = Contract.objects.create(
                name='contract',
                product=Product.objects.first(),
                document=self.test_file,
                description='description for test contract',
                cost=Decimal('12000.00'),
                start_date=date(day=14, month=10, year=2024),
                end_date=date(day=14, month=10, year=2025),
            )
            form_data = {
                'lead': Lead.objects.first().pk,
                'customer_contract': contract.pk,
            }
            response_with_data = self.client.post(
                reverse('customers:customer_create'),
                data=form_data,
                follow=True,
            )
            self.assertEqual(response_with_data.status_code, 200)
            self.assertTrue(Customer.objects.filter(contract=contract.pk).exists())
            contract.delete()

    def test_detail_customer_view(self):
        response = self.client.get(
            reverse(
                'customers:customer_detail',
                kwargs={'pk': self.test_customer.pk}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_update_customer_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'customers:customer_update',
                    kwargs={'pk': self.test_contract.pk}
                )
            )
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            contract = Contract.objects.create(
                name='contract',
                product=Product.objects.first(),
                document=self.test_file,
                description='description for test contract',
                cost=Decimal('12000.00'),
                start_date=date(day=14, month=10, year=2024),
                end_date=date(day=14, month=10, year=2025),
            )
            form_data = {
                'first_name': 'new_f_name',
                'surname': 'new_s_name',
                'last_name': 'new_l_name',
                'email': 'new@mail.ru',
                'phone': '89121292469',
                'ad': Ads.objects.first().pk,
                'contract': contract.pk,
            }
            response_with_data = self.client.post(
                reverse(
                    'customers:customer_update',
                    kwargs={'pk': self.test_customer.pk}
                ),
                data=form_data,
                follos=True,
            )
            self.assertEqual(response_with_data.status_code, 302)

    def test_delete_customer_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'customers:customer_delete',
                    kwargs={'pk': self.test_customer.pk}
                )
            )
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            check_pk_customer = self.test_customer.pk
            response = self.client.post(
                reverse(
                    'customers:customer_delete',
                    kwargs={'pk': self.test_customer.pk}
                )
            )
            self.assertEqual(response.status_code, 302)
            self.assertFalse(Customer.objects.filter(pk=check_pk_customer).exists())
