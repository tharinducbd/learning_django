from django.test import TestCase
from django.urls import reverse

from catalog.models import Author, Genre, Language


# This is for demonstrations only.
# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls) -> None:
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self) -> None:
#         print("setUp: Run once for every test method to set up clean data.")
#         pass

#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)


class AuthorModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Set up non-modified objects used by all test methods.
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f"{author.last_name}, {author.first_name}"
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')


class GenreModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Set up data for the whole TestCase
        cls.genre = Genre.objects.create(name='Test_genre')

    def test_name_label(self):
        field_label = self.genre._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        max_length = self.genre._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_name_help_text(self):
        help_text = self.genre._meta.get_field('name').help_text
        self.assertIn('Enter a book genre', help_text)

    def test_get_absolute_url(self):
        # Genre model has no detail view implemented.
        pass


class LanguageModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.language = Language.objects.create(name="Sinhala")

    def test_name_label(self):
        field_label = self.language._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        max_length = self.language._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_name_help_text(self):
        help_text = self.language._meta.get_field('name').help_text
        self.assertIn('natural language', help_text)
