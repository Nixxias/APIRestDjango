from rest_framework import serializers
from .models import Author, Book, Copy

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    class Meta:
        model = Book
        fields = ['id', 'title', 'year', 'author', 'author_id']
    
    def validate_year(self, value):
        if value < 0: raise serializers.ValidationError("Year cannot be negative.")
        return value

class CopySerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='book')
    class Meta:
        model = Copy
        fields = ['id', 'book_id', 'status']