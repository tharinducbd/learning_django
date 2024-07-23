from typing import Any
from django.db.models.query import QuerySet
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
    paginate_by = 15

    # Overriding default attributes
    # context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains='the')[:10]
    # template_name = 'catalog/book_list.html'

    # Overriding default class methods

    # def get_queryset(self) -> QuerySet[Any]:
    #     return Book.objects.filter(title__icontains='the')[:10]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'Some other data'
        return context


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author
