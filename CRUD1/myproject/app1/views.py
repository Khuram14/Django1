from django.shortcuts import render
from .forms import BookForm
from .models import Book

def book_list(request):
    book= Book.objects.all()
    return render(request,"books/book_list.html",{'object_list':book})