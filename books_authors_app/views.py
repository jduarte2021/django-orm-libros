from django.shortcuts import render, redirect
from .models import Book,Author

def index(request):
    context = {
        'libros': Book.objects.all(),
    }
    return render(request, 'index.html', context)

def autor(request):
    context = {
        'autor': Author.objects.all(),
    }
    return render(request, 'authors.html', context)


def ingresar_libro(request):
    print(request.POST)

    libro = Book.objects.create(
        title   =   request.POST['title'],
        desc    =   request.POST['desc'],
    )

    return redirect("/")


def ingresar_autor(request):
    print(request.POST)
    autor = Author.objects.create(
        first_name  =   request.POST['first_name'],
        last_name   =   request.POST['last_name'],
        notas       =   request.POST['notas'],
    )
    return redirect("/autores")

