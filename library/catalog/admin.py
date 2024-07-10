from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["get_author", "date_of_birth", "date_of_death",]

    def get_author(self, obj):
        return f"{obj.last_name}, {obj.first_name}"
    get_author.short_description = 'Full Name'


# @ line Identical to admin.site.register(Book, BookAdmin)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Customizations for the Model objects list view
    list_display = ("title", "author", "isbn", "display_genre")

    # Customizations for the object detail view
    filter_horizontal = ["genre",]


# @ line Identical to admin.site.register(BookInstance, BookInstanceAdmin)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ["instance", "imprint", "status", "due_back",]

    @admin.display(description="Book Instance")
    def instance(self, obj):
        return f"{obj.id} ({obj.book})"
    # instance.short_description = 'Book Instance'


# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)

admin.site.register(Genre)
admin.site.register(Language)

admin.site.register(Author, AuthorAdmin)
