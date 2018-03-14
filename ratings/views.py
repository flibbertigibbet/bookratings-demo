from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import DUMMY_PASSWORD, RatingsUserCreationForm


def index(request):
    if request.user.is_authenticated():
        return HttpResponse("Hello, world. Here is the ratings site.")
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
            return redirect('index')
        else:
            print(form.cleaned_data)
    else:
        form = RatingsUserCreationForm()
    return render(request, 'signup.html', {'form': form})
