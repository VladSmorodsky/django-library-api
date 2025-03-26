from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Book


# Create your tests here.

class BookApiTestCase(APITestCase):
    """
    Test Book API
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test1111')
        self.admin_user = User.objects.create_superuser(username='admin', password='test1234')
        self.client.force_authenticate(user=self.admin_user)

        self.books_url = reverse('book-list')
        self.book = Book.objects.create(title='Test Book', author='Test Author', genre='Fantasy', publication_year=2025)

    def test_get_books(self):
        """
        Test getting book list
        :return:
        """
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('count'), 1)
        self.assertEqual(response.json().get('results')[0].get('title'), self.book.title)
        self.assertEqual(response.json().get('results')[0].get('author'), self.book.author)

    def test_get_book(self):
        """
        Test getting book detail
        :return:
        """
        url = reverse('book-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), self.book.title)
        self.assertEqual(response.json().get('author'), self.book.author)

    def test_create_book(self) -> None:
        """
        Test creating a book
        :return:
        """
        data = {
            'title': 'Book',
            'author': 'Author',
            'genre': 'Documental',
            'publication_year': 2000,
        }
        response = self.client.post(self.books_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), data.get('title'))
        self.assertEqual(response.json().get('author'), data.get('author'))
        self.assertEqual(response.json().get('genre'), data.get('genre'))
        self.assertEqual(response.json().get('publication_year'), data.get('publication_year'))

    def test_update_book(self) -> None:
        """
        Test updating a book
        :return:
        """
        url = reverse('book-detail', kwargs={'pk': 1})
        data = {
            'title': 'Book',
            'author': 'Author',
            'genre': 'Documental',
            'publication_year': 2000,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), data.get('title'))
        self.assertEqual(response.json().get('author'), data.get('author'))
        self.assertEqual(response.json().get('genre'), data.get('genre'))
        self.assertEqual(response.json().get('publication_year'), data.get('publication_year'))

    def test_delete_book_by_admin(self) -> None:
        """
        Test deleting a book
        :return:
        """
        url = reverse('book-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_by_no_admin_user(self) -> None:
        """
        Test deleting a book by no admin user
        :return:
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('book-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
