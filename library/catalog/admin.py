from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["get_author", "date_of_birth"]

    def get_author(self, obj):
        return f"{obj.last_name}, {obj.first_name}"


class BookAdmin(admin.ModelAdmin):
    # Customizations for the Model objects list view
    list_display = ["title", "author", "isbn",]

    # Customizations for the object detail view
    filter_horizontal = ["genre",]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
