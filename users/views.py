from django.shortcuts import render
from users.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users-profile')  
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = UserForm()
    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Пользователь с таким именем уже существует')
            else:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, 'Регистрация прошла успешно. Войдите в систему.')
                return redirect('users-login')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('users-login')

def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})