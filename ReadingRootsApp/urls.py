from django.urls import path

# importing views from views..py
from .views import *

urlpatterns = [
    path('', home),
    path('addBook/',addBook),
    path('bookadded/',bookAdded),
    path('bookList/',bookList)
]