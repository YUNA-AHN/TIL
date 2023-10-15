from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users' : users
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    # 로그인 되어 있다면 바로 stores로
    if request.user.is_authenticated:
        return redirect('stores:index')
    # 입력이 있다면, form에 request와 POST에 들어온 값 입력
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 유효하다면 로그인! request, get_user
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('stores:index')
    # 암것도 없다면 form 출력
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('stores:index')

def signup(request):
    # 로그인 되어 있다면 바로 stores로
    if request.user.is_authenticated:
        return redirect('stores:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # 입력이 유효하다면
        if form.is_valid():
            # 바로 로그인 시키고 싶다면 user로 받아서 넘겨주기
            user = form.save()
            auth_login(request, user)
            return redirect('stores:index')
    else:
        # 암것도 없다면 form 출력
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)
        
# 연습 겸 추가 : 회원 삭제, 회원 정보 수정, 비밀번호 수정
@login_required
def delete(request):
    user = request.user
    user.delete()
    return redirect('stores:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('stores:index')
    else:
        form = CustomUserChangeForm(isinstance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request, user_pk):
    if request.method == "POST":
        # 이 부분 다른 함수와 다르니가 잘 체크! user/data 순서
        form = PasswordChangeForm(request.user. request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('stores:index')
    else:
        form  = PasswordChangeForm(request.user)
        context = {
            'form':form,
        }
    return render(request, 'accounts/change_password.html', context)