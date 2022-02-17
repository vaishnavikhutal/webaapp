from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def welcome(request):
    return render(request,"welcome.html")

def load_form(request):
    form=BookForm
    return render(request, "index.html",{'form': form})

def add(request):
    form=BookForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    book=Book.objects.all
    return render(request,'show.html',{'book':book})

def edit(request,id):
    book=Book.objects.get(id=id)
    return render(request,'edit.html',{'book':book})

def update(request,id):
    book=Book.objects.get(id=id)
    form=BookForm(request.POST, instance=book)
    form.save()
    return redirect('/show')


def delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/show')

def search(request):
    given_name=request.POST['name']
    book = Book.objects.filter(ename__icontains=given_name)
    return render(request,'show.html',{'book':book})


def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
    return render(request,"login.html")