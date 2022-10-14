from django.contrib import admin
from .models import Author, Publisher, Book
 
@admin.register(Author)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Author = ['author_name']

@admin.register(Publisher)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Publisher = ['publisher', 'country']

@admin.register(Book)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Books = ['title', 'author', 'genre', 'publisher']