from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        # 폼에 대한 유효성 검사
        # 유저 인스턴스 생성
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    #  회원 탈퇴
    user = request.user
    user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    # 회원수정 폼 -> 로직
    if request.method =="POST":
        form = CustomUserChangeForm(request.POST, instance = request.user  )
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        return
    else: # GET
        form  = CustomUserChangeForm(instance = request.user )
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        # 비밀번호를 변경 처리하는 로직
        form = PasswordChangeForm(request.user, request.POST)
    else:
        # 비밀번호 변경
        # PasswordChangeForm: 모델폼이 아니므로, 커스텀 해 줄 필요 없음
        form = PasswordChangeForm(request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)