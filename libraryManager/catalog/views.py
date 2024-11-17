from django.shortcuts import render
from django.http import request,response;
from .models import Book,Author,BookInstance,Genre
from django.db.models import Count
# Create your views here.
def index(request):
    num_of_book = Book.objects.all().count();
    num_of_instances = BookInstance.objects.all().count()
    num_of_instances_available = BookInstance.objects.filter(status='a').count()
    num_of_author = Author.objects.all().count()
    genres_with_book_count = Genre.objects.annotate(
        book_count=Count('book')
        )

    context = {
        'num_book':num_of_book,
        'num_instances':num_of_instances,
        'num_instances_available':num_of_instances_available,
        'num_of_author':num_of_author,
        'genre_list':genres_with_book_count
    }
    return render(request,'index.html',context=context);
    