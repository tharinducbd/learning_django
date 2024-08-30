from django.test import TestCase

from catalog.models import Author


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


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Set up non-modified objects used by all test methods.
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    
