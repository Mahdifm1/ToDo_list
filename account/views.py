from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('before save')
            form.save()
            print('after save')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home_page')
        else:
            print(form.errors)
            return render(request, 'registration/signup.html', {'errors': form.errors, 'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
