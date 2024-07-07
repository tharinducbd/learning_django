from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language


class BookAdmin(admin.ModelAdmin):
    """Customizations for the Model objects list view."""
    list_display = ["title", "author", "isbn"]


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
