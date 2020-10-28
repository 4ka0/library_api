from django.test import TestCase
from django.urls import reverse, resolve

from .models import Book
from .views import BookListView


class TestUrl(TestCase):

    def test_home_page_url_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class TestModel(TestCase):

    def setUp(self):
        Book.objects.create(
            title="My Book",
            subtitle="A Book About Life",
            author="Jon Lee",
            isbn="1234567893548"
        )
    
    def test_model_content(self):
        book = Book.objects.get(id=1)
        title = f'{book.title}'
        subtitle = f'{book.subtitle}'
        author = f'{book.author}'
        isbn = f'{book.isbn}'
        self.assertEqual(title, 'My Book')
        self.assertEqual(subtitle, 'A Book About Life')
        self.assertEqual(author, 'Jon Lee')
        self.assertEqual(isbn, '1234567893548')


class TestView(TestCase):

    def setUp(self):
        Book.objects.create(
            title="My Book",
            subtitle="A Book About Life",
            author="Jon Lee",
            isbn="1234567893548"
        )

    def test_correct_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_view_model_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "My Book", 1)
        self.assertContains(response, "A Book About Life", 1)
        self.assertContains(response, "Jon Lee", 1)
        self.assertContains(response, "1234567893548", 1)
