from django.test import TestCase
from .models import Pessoa
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.urls import reverse

class PessoaTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'apelido': 'josé',
            'nome': 'José Roberto',
            'nascimento': '2000-10-01',
            'stack': ['C#', 'Node', 'Oracle']
        }
        self.invalid_payload = {
            'apelido': 'ana',
            'nome': None,
            'nascimento': '1985-09-23',
            'stack': None
        }
        self.pessoa = Pessoa.objects.create(
            apelido='maria',
            nome='Maria Silva',
            nascimento='1990-05-15',
            stack=['Python', 'Django']
        )

    def test_create_valid_pessoa(self):
        response = self.client.post(
            reverse('pessoa-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_pessoa(self):
        response = self.client.post(
            reverse('pessoa-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_get_valid_pessoa(self):
        response = self.client.get(
            reverse('pessoa-detail', kwargs={'pk': self.pessoa.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['apelido'], self.pessoa.apelido)

    def test_get_invalid_pessoa(self):
        response = self.client.get(
            reverse('pessoa-detail', kwargs={'pk': 9999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_pessoa_found(self):
        response = self.client.get(
            reverse('pessoa-list'),
            {'t': 'maria'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)
        self.assertEqual(response.data[0]['apelido'], self.pessoa.apelido)

    def test_search_pessoa_not_found(self):
        response = self.client.get(
            reverse('pessoa-list'),
            {'t': 'nãoexistente'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_search_pessoa_no_term(self):
        response = self.client.get(
            reverse('pessoa-list')
        )
        # Expecting a list of todas as pessoas
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_pessoa_valid(self):
        updated_data = {
            'apelido': 'maria_updated',
            'nome': 'Maria Souza',
            'nascimento': '1991-06-20',
            'stack': ['Python', 'Django', 'React']
        }
        response = self.client.put(
            reverse('pessoa-detail', kwargs={'pk': self.pessoa.pk}),
            data=updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pessoa.refresh_from_db()
        self.assertEqual(self.pessoa.apelido, 'maria_updated')

    def test_update_pessoa_invalid(self):
        updated_data = {
            'apelido': 'maria_updated',
            'nome': None,
            'nascimento': '1991-06-20',
            'stack': ['Python', 'Django', 'React']
        }
        response = self.client.put(
            reverse('pessoa-detail', kwargs={'pk': self.pessoa.pk}),
            data=updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_delete_pessoa_valid(self):
        response = self.client.delete(
            reverse('pessoa-detail', kwargs={'pk': self.pessoa.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
