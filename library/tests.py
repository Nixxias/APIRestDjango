from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book, Copy

class LibraryTests(APITestCase):
    def setUp(self):
        # Tworzenie danych testowych
        self.author = Author.objects.create(first_name="Jan", last_name="Kowalski")
        self.book = Book.objects.create(title="Test Book", year=2020, author=self.author)
        self.copy = Copy.objects.create(book=self.book, status="AVAILABLE")

    def test_create_author(self):
        url = reverse('author-list')
        data = {'first_name': 'Adam', 'last_name': 'Nowak'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)

    def test_create_book_validation(self):
        """Test walidacji: rok ujemny powinien zwrócić błąd"""
        url = reverse('book-list')
        data = {
            'title': 'Bad Year Book', 
            'year': -5, 
            'author_id': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_books_structure(self):
        """Test czy GET zwraca pełnego autora"""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Sprawdzamy czy w odpowiedzi jest zagnieżdżony słownik 'author'
        self.assertIn('author', response.data)
        self.assertEqual(response.data['author']['id'], self.author.id)

    def test_filter_books_by_author(self):
        """Test parametru authorId"""
        author2 = Author.objects.create(first_name="Anna", last_name="Nowak")
        Book.objects.create(title="Anna's Book", year=2021, author=author2)
        
        url = reverse('book-list')
        response = self.client.get(url, {'authorId': self.author.id})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_create_copy(self):
        url = reverse('copy-list')
        data = {'book_id': self.book.id, 'status': 'BORROWED'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Copy.objects.count(), 2)