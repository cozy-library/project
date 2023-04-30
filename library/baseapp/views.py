from django.shortcuts import render, redirect, HttpResponse
from .models import Book
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
import os
from django.http import FileResponse
# Create your views here.


def homePage(request):
    return render(request, 'baseapp/home1.html', {})

def about(request):
    return render(request, 'baseapp/about.html', {})

def bookPage(request):
    # books = Book.objects.all()
    query = request.GET.get('q')
    
    if query:
        # Filter the books based on the search query
        books = Book.objects.filter(Q(title__icontains=query) | Q(description__icontains = query))
        if books:
            context = {"books": books}
            return render(request, 'baseapp/book2.html', context )
        else:
            messages.info(request, "No such book available")
            return render(request, 'baseapp/book2.html', {})
            
    else:
        # If no search query is provided, return all books
        books = Book.objects.all()
        # messages.info(request, "The searched book is not available")
    context = {
        "books": books
    }
    return render(request, 'baseapp/book2.html', context )

def signup(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
    #     user = User.objects.create_user(username=username,  email=email, password=password)
    #     user.save()
    #     print("success")
    #     return redirect('/')
    # else:
    #     return render(request, 'baseapp/signup1.html')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Already exist")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
                return redirect('signup')
        
            else:
            
                user = User.objects.create_user(username=username,  email=email, password=password)
                user.save()
                messages.success(request, "Account successfully created")
                return redirect('loginPage')
        else:
            messages.error(request, "Password mismatched")
            return redirect("signup")
    return render(request, 'baseapp/signup1.html', {})

def loginPage(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            # log in the user
             auth.login(request, user)
            
             return redirect('home')
        else:
            messages.error(request, "You don't have an account")
            return redirect('loginPage')
     else:
         return render(request, 'baseapp/login1.html', {})
    
    
def logout(request):
    auth.logout(request)
    return redirect('home') 
     
     

# downloading the book
def download_book(request, book_id):
    book = Book.objects.get(id=book_id)
    file_path = book.file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        messages.warning(request, "Oops!, something went wrong.")
     
     
     
    #            
    


def search(request):
    query = request.GET.get('q')
    results = Book.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'results': results})    
        
    


