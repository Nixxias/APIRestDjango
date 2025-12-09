from rest_framework import viewsets
from .models import Author, Book, Copy
from .serializers import AuthorSerializer, BookSerializer, CopySerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.request.query_params.get('authorId')
        if author_id:
            queryset = queryset.filter(author__id=author_id)
        return queryset

class CopyViewSet(viewsets.ModelViewSet):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer