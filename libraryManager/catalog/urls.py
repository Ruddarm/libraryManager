from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
# from views import getHello
from  . import views;


urlpatterns = [
    path('', views.index,name='index'),
    path('books/',views.BookListView.as_view(),name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),


    # path('catalog/',include('catalog.urls')),
    # path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
