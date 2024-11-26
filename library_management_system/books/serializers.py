from rest_framework import serializers
from .models import Book, BorrowHistory

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'genre', 'publication_date', 'stock_quantity')

class BorrowHistorySerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = BorrowHistory
        fields = ('book', 'user', 'borrowed_at', 'returned_at')
