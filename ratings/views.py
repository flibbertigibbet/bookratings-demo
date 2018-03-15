from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render

from .forms import DUMMY_PASSWORD, RatingsForm, RatingsUserCreationForm
from .middleware import USERNAME_COOKIE


def index(request):
    if request.user.is_authenticated():
        response = ratings(request)
        if USERNAME_COOKIE not in request.COOKIES:
            response.set_cookie(USERNAME_COOKIE, request.user.username)
        return response
    else:
        return redirect('signup')


def signup(request):
    if request.method == 'POST':
        form = RatingsUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=DUMMY_PASSWORD)
            login(request, user)
            response = redirect('index')
            response.set_cookie(USERNAME_COOKIE, username)
            return response
    else:
        form = RatingsUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def ratings(request):
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RatingsForm()
    return render(request, 'ratings.html', {'form': form})
