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
