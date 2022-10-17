from django.test import TestCase
from django .urls import reverse
from rest_framework.test import APITestCase
from books.models import Book
from rest_framework import status
# Create your tests here.


class TestAPI(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom christie",
            isbn="1234567890123",
        )

    def test_api_list_view(self):
        response = self.client.get(reverse("book_list"))
        print(response)
        self.assertEqual(200, response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.all().count(), 1)
