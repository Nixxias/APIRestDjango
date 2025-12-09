from rest_framework import serializers
from .models import Author, Book, Copy

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

    def validate(self, data):
        if not data.get('first_name') or not data.get('last_name'):
            raise serializers.ValidationError("First name and last name cannot be empty.")
        return data

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    # ZMIANA TUTAJ: Zmieniamy nazwę pola na authorId, żeby pasowało do testów
    authorId = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), 
        source='author', 
        write_only=True
    )

    class Meta:
        model = Book
        # ZMIANA TUTAJ: Dodajemy authorId do listy pól
        fields = ['id', 'title', 'year', 'author', 'authorId']

    def validate_year(self, value):
        if value < 0:
            raise serializers.ValidationError("Year cannot be negative.")
        return value

    def validate_title(self, value):
        if not value.strip():
             raise serializers.ValidationError("Title cannot be empty.")
        return value

class CopySerializer(serializers.ModelSerializer):
    # Tutaj testy mogą używać bookId lub book_id, zazwyczaj DTO w tym zadaniu to bookId
    # Dla bezpieczeństwa zróbmy podobny manewr co przy książce, choć testy egzemplarzy są prostsze
    bookId = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='book'
    )
    
    class Meta:
        model = Copy
        fields = ['id', 'bookId', 'status']