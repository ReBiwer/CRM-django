from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User, Group

from products.models import Product
from .models import Contract
from decimal import Decimal
from datetime import date


class TestAppContracts(TestCase):
    fixtures = ['backup.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_manager = User.objects.create_user(
            username='manager',
            password='qwerty123@',
        )
        cls.test_manager.groups.add(Group.objects.get(name='Manager'))
        cls.test_product = Product.objects.create(
            name='test_product',
            description='test_description',
            cost=Decimal('2999.99'),
            created_by=cls.test_manager,
        )
        cls.test_file = SimpleUploadedFile(
            name='test_file.txt',
            content=b'This if a test file',
            content_type='text/plain'
        )
        cls.test_contract = Contract.objects.create(
            name='test_contract',
            product=cls.test_product,
            document=cls.test_file,
            description='description for test contract',
            cost=Decimal('12000.00'),
            start_date=date(day=14, month=10, year=2024),
            end_date=date(day=14, month=10, year=2025),
        )

    @classmethod
    def tearDownClass(cls):
        cls.test_manager.delete()
        cls.test_product.delete()
        cls.test_contract.delete()

    def setUp(self):
        self.client.force_login(self.test_manager)

    def tearDown(self):
        self.client.logout()

    def test_list_contracts_view(self):
        response = self.client.get(reverse('contracts:contracts'))
        self.assertEqual(response.status_code, 200)
        for i_contract in Contract.objects.all():
            with self.subTest(f'Test for the presence ad: {i_contract.name}'):
                self.assertContains(response, i_contract, html=True)

    def test_create_contract_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(reverse('contracts:contract_create'))
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            form_data = {
                'name': 'test_contract',
                'product': self.test_product,
                'document': self.test_file,
                'description': 'someone description',
                'cost': Decimal('13990.00'),
                'start_date': date(day=14, month=10, year=2024),
                'end_date': date(day=14, month=10, year=2025),
            }
            response_with_data = self.client.post(
                reverse('contracts:contract_create'),
                data=form_data,
                follow=True,
            )
            self.assertEqual(response_with_data.status_code, 200)
            self.assertTrue(Contract.objects.filter(name=form_data['name']).exists())

    def test_detail_contract_view(self):
        response = self.client.get(
            reverse(
                'contracts:contract_detail',
                kwargs={'pk': self.test_contract.pk}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_update_contract_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'contracts:contract_update',
                    kwargs={'pk': self.test_contract.pk}
                )
            )
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            form_data = {
                'name': 'new_name_contract',
                'product': self.test_product,
                'document': self.test_file,
                'description': 'new_someone description',
                'cost': Decimal('23990.00'),
                'start_date': date(day=18, month=11, year=2024),
                'end_date': date(day=18, month=11, year=2025),
            }
            response_with_data = self.client.post(
                reverse('contracts:contract_update', kwargs={'pk': self.test_contract.pk}),
                data=form_data,
                follow=True,
            )
            self.assertEqual(response_with_data.status_code, 200)

    def test_delete_contract_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'contracts:contract_delete',
                    kwargs={'pk': self.test_contract.pk}
                )
            )
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            new_contract = Contract.objects.create(
                name='test_contract',
                product=self.test_product,
                document=self.test_file,
                description='description for test contract',
                cost=Decimal('12000.00'),
                start_date=date(day=14, month=10, year=2024),
                end_date=date(day=14, month=10, year=2025),
            )
            response = self.client.post(
                reverse(
                    'contracts:contract_delete',
                    kwargs={'pk': new_contract.pk}
                )
            )
            self.assertEqual(response.status_code, 302)
