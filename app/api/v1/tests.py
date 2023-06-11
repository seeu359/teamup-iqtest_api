from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


class TestEndpointsTesting(TestCase):

    fixtures = [
        'test.json',
        'iqtest.json',
        'eqtest.json',
    ]

    def setUp(self):
        self.client = Client()
        self.test_obj = self.client.post(reverse('create_test'))
        self.login = self.test_obj.json().get('login')
        self.content_type = 'application/json'

    def test_create_test_obj(self):
        response = self.client.post(reverse('create_test'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        login = response.json().get('login')
        self.assertEqual(len(login), 10)
        self.assertTrue(login.isalpha())

    def test_save_iq_test(self):
        response = self.client.post(
            reverse('iq_save'), {'login': self.login, 'result': 46}, content_type=self.content_type
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('login'), self.login)
        self.assertEqual(response.json().get('result'), 46)

    def test_iq_test_with_incorrect_data(self):
        response = self.client.post(
            reverse('iq_save'), {'login': self.login, 'result': 55},
        )

        response2 = self.client.post(
            reverse('iq_save'), {'login': self.login, 'result': -5},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_save_eq_test(self):
        array_data = ['A', 'B', 'C', 'D', 'E']
        response = self.client.post(
            reverse('eq_save'), data={'login': self.login, 'result': array_data},
            content_type='application/json'
        )

        response_result = response.json().get('result')
        response_login = response.json().get('login')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_result, array_data)
        self.assertEqual(response_login, self.login)

    def test_save_eq_test_with_incorrect_data(self):
        wrong_array_data1 = ['A', 'B', 'C', 'D']
        wrong_array_data2 = ['A', 'B', 'C', 'D', 'D']

        response1 = self.client.post(
            reverse('eq_save'), data={'login': self.login, 'result': wrong_array_data1},
            content_type='application/json'
        )
        response2 = self.client.post(
            reverse('eq_save'), data={'login': self.login, 'result': wrong_array_data2},
            content_type='application/json'
        )

        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_test(self):
        iq_result = 46
        eq_result = ['A', 'B', 'C', 'D', 'E']

        self.client.post(
            reverse('iq_save'), {'login': self.login, 'result': 46}, content_type=self.content_type
        )
        self.client.post(
            reverse('eq_save'), data={'login': self.login, 'result': eq_result},
            content_type='application/json'
        )

        response = self.client.get(reverse('test_detail'), data={'login': self.login})
        self.assertTrue(response.json()['tests']['iqtest']['result'], iq_result)
        self.assertTrue(response.json()['tests']['eqtest']['result'], eq_result)
