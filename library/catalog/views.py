from django.shortcuts import render

from .models import Author, Book, BookInstance, Genre


def index(request):
    """View function for hompe page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_genres = Genre.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_genres": num_genres,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }

    return render(request, "catalog/index.html", context)
