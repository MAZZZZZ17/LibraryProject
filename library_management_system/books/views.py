from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Book, BookReservation
from .serializers import BookSerializer


@login_required
def user_profile_and_books(request):
    user = request.user
    books = Book.objects.all().order_by('title')

    title = request.GET.get('title', '')
    genre = request.GET.get('genre', '')

    if title:
        books = books.filter(title__icontains=title)
    if genre:
        books = books.filter(genre__name__icontains=genre)

    paginator = Paginator(books, 5)  # 5 books per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'users/profile.html', {'user': user, 'books': page_obj})


class BookListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all().order_by('title')

        title = request.query_params.get('title')
        genre = request.query_params.get('genre')

        if title:
            books = books.filter(title__icontains=title)
        if genre:
            books = books.filter(genre__name__icontains=genre)

        paginator = Paginator(books, 5)
        page_number = request.query_params.get('page', 1)
        page_obj = paginator.get_page(page_number)

        serializer = BookSerializer(page_obj, many=True)
        return Response(serializer.data)


class BookReservationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        existing_reservation = BookReservation.objects.filter(book=book, user=request.user).first()

        if existing_reservation and not existing_reservation.is_expired():
            return Response({"error": "You already have an active reservation for this book."}, status=status.HTTP_400_BAD_REQUEST)

        if book.stock_quantity > 0:
            if existing_reservation:
                existing_reservation.delete()

            BookReservation.objects.create(book=book, user=request.user)
            book.stock_quantity -= 1
            book.save()
            return Response({"message": "Book reserved successfully!"}, status=status.HTTP_201_CREATED)

        return Response({"error": "Book is out of stock."}, status=status.HTTP_400_BAD_REQUEST)
