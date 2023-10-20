from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404

from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    # 이미 로그인이 되어 있다면
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def logout(request):
    auth_logout(request)
    return redirect('boards:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    # 이미 로그인이 되어 있다면
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    } 
    return render(request, 'accounts/signup.html', context)

def profile(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)
    context = {
        'person': person
    }
    return render(request, 'accounts/profile.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk = user_pk)
    if request.user != person:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.pk)