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
