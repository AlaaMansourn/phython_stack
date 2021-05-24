from django.shortcuts import render,redirect
from books_authors_app.models import *


def index(request):

    all_books=Book.objects.all()
    context={"books":all_books}
    
   

    return render(request,'index.html',context)
# Create your views here.

def booktemplate(request,id):
    this_book=Book.objects.get(id=id)
    authors=this_book.authors.all()
    all_author=Author.objects.all()
    context={"book":this_book,"authors":authors,"all_author":all_author}

    return render(request,'index2.html',context)



def gettitle(request):
    if request.method=='GET':
    
        title= request.GET['title']
        description=request.GET['description']
        Book.objects.create(title=title,desc=description)   


    return redirect("/")


def addauthor(request):
    if request.method=='GET':
        id=request.GET['book_id']
        author_id=request.GET['auth']

        print("i got a author_id"+author_id)
        this_book=Book.objects.get(id=id)
        this_author=Author.objects.get(id=author_id)

        this_book.authors.add(this_author)



    return redirect("/"+id)


def index4(request):
    
    all_authors=Author.objects.all()
    context={"authors":all_authors}
    
   

    return render(request,'index4.html',context)


def authorToadd(request):
    if request.method=='GET':
    
        first_name= request.GET['fname']
        last_name=request.GET['lname']
        Author.objects.create(first_name=first_name,last_name=last_name)   


    return redirect("/author"+id)

def authortemplate(request,id):

    this_author=Author.objects.get(id=id)
    books=this_author.books.all()
    all_book=Book.objects.all()
    context={"author":this_author,"books":books,"all_book":all_book}

    return render(request,'index5.html',context)


def authorToadd(request):
    if request.method=='GET':
        
        first_name= request.GET['fname']
        last_name=request.GET['lname']
        Author.objects.create(first_name=first_name,last_name=last_name)   


    return redirect("/author")

def addbookto(request):
    if request.method=='GET':
        id=request.GET['author_id']
        book_id=request.GET['boo']

        
        this_author=Author.objects.get(id=id)
        this_book=Book.objects.get(id=book_id)

        this_author.books.add(this_book)



    return redirect("/author/"+id)