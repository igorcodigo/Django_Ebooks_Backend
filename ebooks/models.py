from django.db import models
from django.contrib.auth.models import User  # Para relacionar e-books a usuários

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Ebook(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    authors = models.ManyToManyField(Author, related_name="author_ebooks")  
    genres = models.ManyToManyField(Genre, related_name="genre_ebooks") 
    publication_date = models.DateField()
    num_pages = models.PositiveIntegerField()
    cover_photo = models.ImageField(upload_to='book_covers/', blank=True, null=True)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_ebooks")  # Quem criou
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name_plural = "Ebook"
