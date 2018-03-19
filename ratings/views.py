from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render

from .forms import DUMMY_PASSWORD, AddBookForm, RateBookForm, RatingsUserCreationForm
from .middleware import USERNAME_COOKIE
from .models import Book, BookRating


def home(request):
    user_books = Book.objects.filter(added_by=request.user)
    user_ratings = BookRating.objects.filter(user=request.user)
    return render(request, 'home.html', {
                  'user_added_books': user_books,
                  'user_added_ratings': user_ratings})


def index(request):
    if request.user.is_authenticated():
        response = home(request)
        if USERNAME_COOKIE not in request.COOKIES:
            response.set_cookie(USERNAME_COOKIE, request.user.username)
        return response
    else:
        return redirect('signup')


def signup(request):
    if request.method == 'POST':
        form = RatingsUserCreationForm(request.POST)
        username = form.data['username']
        # create user if user does not exist
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
        user = authenticate(username=username, password=DUMMY_PASSWORD,
                            backend='django.contrib.auth.backends.ModelBackend')
        if user:
            login(request, user)
        response = redirect('index')
        response.set_cookie(USERNAME_COOKIE, username)
        return response
    else:
        form = RatingsUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def rate_book(request):
    if request.method == 'POST':
        form = RateBookForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RateBookForm(user=request.user)
    return render(request, 'rate_book.html', {'form': form})


def logout_view(request):
    logout(request)
    response = redirect('index')
    if USERNAME_COOKIE in request.COOKIES:
        response.delete_cookie(USERNAME_COOKIE)
    return response


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddBookForm(user=request.user)
    return render(request, 'add-book.html', {'form': form})
