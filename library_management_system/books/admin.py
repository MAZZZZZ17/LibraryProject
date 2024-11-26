from django.contrib import admin
from .models import Book, Author, Genre, BorrowHistory, BookReservation

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_genres', 'publication_date', 'stock_quantity')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'genre__name')
    list_filter = ('genre', 'publication_date')
    filter_horizontal = ('genre',)

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])
    get_genres.short_description = 'Genres'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BorrowHistory)
class BorrowHistoryAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrowed_at', 'returned_at')
    list_filter = ('borrowed_at', 'returned_at')

@admin.register(BookReservation)
class BookReservationAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'reserved_until')
    list_filter = ('reserved_until',)
