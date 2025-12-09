from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, CopyViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'copies', CopyViewSet, basename='copy')

urlpatterns = [
    path('', include(router.urls)),
]
