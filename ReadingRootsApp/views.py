from django.shortcuts import render
from .models import *
from django.shortcuts import redirect


# Create your views here.

def home(request):
    return render(request, "home.html")

def addBook(request):

    genre = Genre.objects.all()
    lang = Language.objects.all()

    return render(request,"addBook.html",{'genre':genre,'lang':lang})

def bookAdded(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        lang = request.POST.get('language')
        uploaded_at = request.POST.get('uploaded_at')

        book = Book.objects.create(Name=name,Author=author,added_on=uploaded_at)
        gen = Genre.objects.get(G_name=genre)
        gen.save()
        lan = Language.objects.get(L_name=lang)
        lan.save()
        book.Genres.add(gen)
        book.Languages.add(lan)
        book.save()
        

        return redirect(bookList)


def bookList(request):

    books = Book.objects.all()
    return render(request,'books.html',{'books':books})