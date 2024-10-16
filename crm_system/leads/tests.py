from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group

from .models import Lead
from ads.models import Ads


class TestLeadApp(TestCase):
    fixtures = ['backup.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_operator = User.objects.create_user(
            username='operator',
            password='qwerty123@',
        )
        cls.test_operator.groups.add(Group.objects.get(name='Operator'))
        cls.test_lead = Lead.objects.create(
            first_name='test_f_name',
            surname='test_s_name',
            last_name='test_l_name',
            email='test@mail.ru',
            phone='89091260929',
            ad=Ads.objects.first(),
        )

    @classmethod
    def tearDownClass(cls):
        cls.test_operator.delete()

    def setUp(self):
        self.client.force_login(self.test_operator)

    def tearDown(self):
        self.client.logout()

    def test_list_lead_view(self):
        response = self.client.get(reverse('leads:leads'))
        self.assertEqual(response.status_code, 200)
        for i_lead in Lead.objects.all():
            with self.subTest(f'Test for presence lead: {i_lead.first_name}'):
                self.assertContains(response, f'{i_lead.last_name} {i_lead.first_name}', html=True)

    def test_create_lead_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(reverse('leads:lead_create'))
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            form_data = {
                'first_name': 'f_name',
                'surname': 's_name',
                'last_name': 'l_name',
                'email': 'mail@mail.ru',
                'phone': '89121292469',
                'ad': Ads.objects.first().pk,
            }
            response_with_data = self.client.post(
                reverse('leads:lead_create'),
                data=form_data,
                follow=True,
            )
            self.assertEqual(response_with_data.status_code, 200)
            self.assertTrue(
                Lead.objects.filter(first_name=form_data['first_name']).exists()
            )

    def test_detail_lead_view(self):
        response = self.client.get(
            reverse(
                'leads:lead_detail',
                kwargs={'pk': self.test_lead.pk}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_update_lead_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'leads:lead_update',
                    kwargs={'pk': self.test_lead.pk}
                )
            )
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            form_data = {
                'first_name': 'new_f_name',
                'surname': 'new_s_name',
                'last_name': 'new_l_name',
                'email': 'new@mail.ru',
                'phone': '89121292469',
                'ad': Ads.objects.first().pk,
            }
            response_with_data = self.client.post(
                reverse(
                    'leads:lead_update',
                    kwargs={'pk': self.test_lead.pk}
                ),
                data=form_data,
                follow=True,
            )
            self.assertEqual(response_with_data.status_code, 200)
            self.assertTrue(Lead.objects.filter(first_name=form_data['first_name']))

    def test_delete_lead_view(self):
        with self.subTest('Test get method'):
            response = self.client.get(
                reverse(
                    'leads:lead_delete',
                    kwargs={'pk': self.test_lead.pk}
                )
            )
            self.assertEqual(response.status_code, 200)

        with self.subTest('Test post method'):
            check_pk_lead = self.test_lead.pk
            response = self.client.post(
                reverse(
                    'leads:lead_delete',
                    kwargs={'pk': self.test_lead.pk}
                )
            )
            self.assertEqual(response.status_code, 302)
            self.assertFalse(Lead.objects.filter(pk=check_pk_lead).exists())
