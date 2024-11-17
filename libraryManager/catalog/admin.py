from django.contrib import admin
from .models import Book,BookInstance,Genre,Author,Language

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
# Register your models here.
