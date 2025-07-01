from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm  , UserUpdateForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.has_portfolio = user_form.cleaned_data.get('has_portfolio', False)
            profile.save()
            
            login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()

    return render(request, 'auth/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def register_view(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.has_portfolio = user_form.cleaned_data.get('has_portfolio', False)
            profile.save()
            
            login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()

    return render(request, 'auth/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Xush kelibsiz, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Login yoki parol noto'g'ri")
        else:
            messages.error(request, "Login yoki parol noto'g'ri")
    else:
        form = LoginForm()
    
    return render(request, 'auth/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Hisobdan muvaffaqiyatli chiqdingiz.")
    return redirect('home')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profil muvaffaqiyatli yangilandi!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
    
    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })