from django.test import TestCase
from django.urls import reverse

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
