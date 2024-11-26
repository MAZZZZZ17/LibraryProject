from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now, timedelta

User = get_user_model()

class Author(models.Model):
    first_name = models.CharField(max_length=100, default='Unknown')
    last_name = models.CharField(max_length=100, default='unknown')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

def get_default_author():
    if Author.objects.exists():
        return Author.objects.first()
    return None

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, default=get_default_author
    )
    genre = models.ManyToManyField(Genre, related_name='books')
    publication_date = models.DateField()
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class BorrowHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_history')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(default=now)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} borrowed {self.book.title}"

def get_default_reserved_until():
    return now() + timedelta(days=1)

class BookReservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_until = models.DateTimeField(default=get_default_reserved_until)


    def is_expired(self):
        return now() > self.reserved_until

    def __str__(self):
        return f"{self.user} reserved {self.book.title}"
