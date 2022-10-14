from django.db import models
from django.contrib.auth.models import User

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=30,null=True)
    country = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.publisher_name

class Author(models.Model):
    author_name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    choice = [
        ('drama', 'Drama'),
        ('fiction', 'Fiction'),
        ('love story', 'Love Story'),
        ('science fiction', 'Science Fiction'),
        ('mystery', 'Mystery'),
    ]
    genre = models.CharField(max_length=20,choices=choice)
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

