from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Copy(models.Model):
    STATUS_CHOICES = [('AVAILABLE', 'Dostepna'), ('BORROWED', 'Wypozyczona')]
    book = models.ForeignKey(Book, related_name='copies', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')
