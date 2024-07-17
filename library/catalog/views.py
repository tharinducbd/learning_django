from django.shortcuts import render
from django.views import generic

from .models import Author, Book, BookInstance, Genre


def index(request):
    """View function for hompe page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_genres = Genre.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Books that have 'the' in the title
    num_books_title_contains_the = Book.objects.filter(title__icontains='the').count()

    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_genres": num_genres,
        "num_instances_available": num_instances_available,
        "num_books_title_contains_the": num_books_title_contains_the,
        "num_authors": num_authors,
    }

    return render(request, "catalog/index.html", context)


class BookListView(generic.ListView):
    model = Book

    # Overriding default attributes
    # context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains='the')[:10]
    # template_name = 'catalog/book_list.html'
