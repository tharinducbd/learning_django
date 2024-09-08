import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from catalog.models import Author


class AuthorListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Create 12 authors for pagination tests
        num_authors = 12

        for author_id in range(num_authors):
            Author.objects.create(
                first_name=f"Dominique {author_id}",
                last_name=f"Surname {author_id}",
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('catalog:authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('catalog:authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('catalog:authors'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('is_paginated', response.context)
        # self.assertTrue('is_paginated' in response.context)     # Similar to previous!
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['author_list']), 10)

    def test_lists_all_authors(self):
        # Get the second page and check if it has exactly 2 items.
        response = self.client.get(reverse('catalog:authors')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('is_paginated', response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['author_list']), 2)


# Get user model from settings
from django.contrib.auth import get_user_model
User = get_user_model()

from catalog.models import BookInstance, Book, Genre, Language

class LoanedBookInstancedByUserListViewTests(TestCase):
    def setUp(self) -> None:
        # Create two users
        test_user_1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user_2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user_1.save()
        test_user_2.save()

        # Create a book
        test_author = Author.objects.create(first_name='John', last_name='Smith')
        test_genre = Genre.objects.create(name='Fantasy')
        test_language = Language.objects.create(name='English')
        test_book = Book.objects.create(
            title='Book title',
            summary='My book summary',
            isbn='ABCDEFG',
            author=test_author,
            language=test_language
        )

        # Create genre as a post-step
        genre_objects_for_book = Genre.objects.all()
        test_book.genre.set(genre_objects_for_book) # Direct assignment of many-to-many types not allowed!
        test_book.save()

        # Create 30 BookInstance objects
        num_book_copies = 30
        for book_copy in range(num_book_copies):
            return_date = timezone.localtime() + datetime.timedelta(days=book_copy%5)
            the_borrower = test_user_1 if book_copy % 2 else test_user_2
            status = 'm'
            BookInstance.objects.create(
                book=test_book,
                imprint='Unlikely Imprint, 2024',
                due_back=return_date,
                status=status,
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('catalog:my-borrowed'))
        self.assertRedirects(response, '/accounts/login/?next=/catalog/mybooks/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('catalog:my-borrowed'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')

        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'catalog/bookinstance_list_borrowed_user.html')

    def test_only_borrowed_books_in_list(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('catalog:my-borrowed'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

        # Check that initially we don't have any books in list (none on loan)
        self.assertTrue('bookinstance_list' in response.context)
        self.assertEqual(len(response.context['bookinstance_list']), 0)

        # Now change all books to be on loan
        books = BookInstance.objects.all()[:10]

        for book in books:
            book.status = 'o'
            book.save()

        # Check that now we have borrowed books in the list
        response = self.client.get(reverse('catalog:my-borrowed'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

        self.assertTrue('bookinstance_list' in response.context)

        # Confirm all books belong to testuser1 and are on loan
        for bookitem in response.context['bookinstance_list']:
            self.assertEqual(response.context['user'], bookitem.borrower)
            self.assertEqual(bookitem.status, 'o')

    def test_pages_ordered_by_due_date(self):
        # Change all books to be on loan
        for book in BookInstance.objects.all():
            book.status = 'o'
            book.save()

        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('catalog:my-borrowed'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

        # Confirm that of the items, only 10 are displayed due to pagination.
        self.assertEqual(len(response.context['bookinstance_list']), 10)
