from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.


def login(request):
    if request.method == "POST":
        # 로그인 처리
        # 로그인 폼 (일반 Form O, ModelForm X)
        form = AuthenticationForm(request, request.POST)
        # 유효성 검사
        if form.is_valid():
            # 로그인을 과정 -> 서버에 "session 생성"
            # (=> django_session 테이블 데이터 추가...)
            user = form.get_user()
            auth_login(request, user)
            return redirect("articles:index")
    else:  # 'GET'
        # 로그인 폼 (일반 Form O, ModelForm X)
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    # 로그아웃 처리
    # 1. 서버에 있는 django_session 세션값이 삭제
    # 2. 클라이언트에서 쿠키값 삭제
    # => logout 함수를 통해서 수행 가능!
    auth_logout(request)
    return redirect('articles:index')
