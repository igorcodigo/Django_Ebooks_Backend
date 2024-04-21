# Importa o módulo 'models' do Django para definir modelos de banco de dados
from django.db import models
# Importa o modelo 'User' do Django para associar e-books a usuários do sistema
from django.contrib.auth.models import User

# Define o modelo 'Author' para representar autores
class Author(models.Model):
    # Define o primeiro nome do autor, limitado a 100 caracteres
    first_name = models.CharField(max_length=100)
    # Define o sobrenome do autor, limitado a 100 caracteres
    last_name = models.CharField(max_length=100)

    # Retorna uma representação legível do autor, combinando o primeiro nome e o sobrenome
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Define o modelo 'Genre' para representar gêneros de e-books
class Genre(models.Model):
    # Define o nome do gênero, limitado a 100 caracteres, com a restrição de ser único (sem duplicatas)
    name = models.CharField(max_length=100, unique=True)

    # Retorna o nome do gênero como representação legível
    def __str__(self):
        return self.name

# Define o modelo 'Ebook' para representar livros digitais
class Ebook(models.Model):
    # Define o título do e-book, com limite de 200 caracteres
    title = models.CharField(max_length=200)
    # Campo para resumo do e-book, sem limite específico de caracteres, mas opcional (pode ser deixado em branco)
    summary = models.TextField(blank=True)
    # Relacionamento muitos-para-muitos com autores, para que um e-book possa ter vários autores
    authors = models.ManyToManyField(Author, related_name="author_ebooks")
    # Relacionamento muitos-para-muitos com gêneros, para que um e-book possa pertencer a vários gêneros
    genres = models.ManyToManyField(Genre, related_name="genre_ebooks")
    # Campo para a data de publicação do e-book
    publication_date = models.DateField()
    # Número de páginas do e-book, que deve ser um número inteiro positivo
    num_pages = models.PositiveIntegerField()
    # Campo para a imagem de capa do e-book, com a opção de ser deixado em branco ou nulo
    cover_photo = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    # Relacionamento com o usuário que criou o e-book, com a opção de ser nulo e comportamento de SET_NULL ao excluir o usuário
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_ebooks")
    # Campo para armazenar a data e hora de criação do registro do e-book, preenchido automaticamente
    created_at = models.DateTimeField(auto_now_add=True)
    # Campo para armazenar a data e hora de atualização do registro do e-book, atualizado automaticamente
    updated_at = models.DateTimeField(auto_now=True)

    # Retorna o título do e-book como representação legível
    def __str__(self):
        return self.title
    
    # Define metadados para o modelo, especificando que o nome plural de 'Ebook' deve ser "Ebook"
    class Meta: 
        verbose_name_plural = "Ebook"
