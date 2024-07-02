from django.db import models
from django.urls import reverse     # required for get_absolute_url()

from django.db.models import UniqueConstraint   # Constrain fields to unique values
from django.db.models.functions import Lower    # Returns lower cased value of field


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
    )

    def __str__(self) -> str:
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        constrains = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message="Genre already exists (case insensitive match)"
            ),
        ]


class Book(models.Model):
    """Model representing a book (but not specific copy of a book)."""
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    # Author as a string rather than an object, because it hasn't been declared yet

    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book",
    )
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                  '">ISBN number</a>',
    )

    genre = models.ManyToManyField(
        Genre,
        help_text="Select a genre for this book",
    )
    # ManyToMany because each genre can have many books and a book can have multiple genres

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
