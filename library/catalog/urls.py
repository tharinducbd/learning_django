from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

# For library members
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

# For librarians. Need 'can_mark_returned' permisson
urlpatterns += [
    path('borrowed/', views.LoanedBooksByAllUsersListView.as_view(), name='all-borrowed'),
]

# For librarians. Need 'can_mark_renew' permission
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

# For librarians. Need relevant permission from admin.
urlpatterns += [
    path('author/create', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete', views.AuthorDelete.as_view(), name='author-delete'),
    path('book/create', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update', views.BookUpdate.as_view(), name='book-update'),
]
