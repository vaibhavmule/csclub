from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from jobboard.models import Job


def home(request):
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs.html', {'jobs': jobs})


def about(request):
    return render(request, 'about.html')


def privacy(request):
    return render(request, 'privacy.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
