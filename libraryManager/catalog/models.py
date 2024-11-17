from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid

class Genre(models.Model):
    name= models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genere (e.g Science , Frition , French , Poetry etc)" )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("genre-detial", args=[str[self.id]]);
    
    class Meta:
        constraints=[
            UniqueConstraint(Lower('name'),name='genre_name_case_insensitive_unique',violation_error_message='Genre Already exists (case insensitive match)'),
        ]
class Language(models.Model):
    name= models.CharField(max_length=200, unique=True,help_text="Enter a language of the book")
    def get_absolute_url(self):
        """Returns the url to access a particular language instance."""
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            ),
        ]

    
# Create your models here.
class Book(models.Model):
    title=  models.CharField(max_length=200)
    author = models.ForeignKey("author",on_delete=models.RESTRICT,null=True)
    summary = models.TextField(max_length=1000,help_text="Enter Breif Descripiton of the book")
    isbn = models.CharField('ISBN',max_length=13,help_text='13Chrateer IBSN NUmber',unique=True)
    genre = models.ManyToManyField(Genre,help_text='Select a genre for this book')
    language = models.ForeignKey(
        Language,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.title;
    def get_absolute_url(self):
        return reverse("book-details", args=[str(self.id)])
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    
#create book instance model 
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,help_text="Unique id for this particualar boo across library")
    book:Book = models.ForeignKey(Book,on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)
    Loan_Status=(('m','Maintenance'),('o','on loan'),('a','available'),('r','reserved'))
    status = models.CharField(max_length=1,choices=Loan_Status,blank=True,help_text='Book avilability')
    
    class Meta:
        ordering = ['due_back']
        
    def __str__(self):
        return f"{self.id} ({self.book.title})"
        
        
class Author(models.Model):
    """Represent an author """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField(null=True,blank=True)
    
    class Meta:
        ordering = ['last_name','first_name']
        
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])
    
