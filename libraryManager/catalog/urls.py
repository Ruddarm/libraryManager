from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
# from views import getHello
from  . import views;


urlpatterns = [
    path('hello/', views.getHello),
    # path('catalog/',include('catalog.urls')),
    # path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
