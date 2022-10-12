from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):    # 회원가입 함수
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():     # POST로 요청 시 회원가입 진행
            form.save()
            username = form.cleaned_data.get('username')       # form.cleaned_data : 폼의 입력값을 개별적으로 얻고 싶을 때 사용
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)   # 사용자 인증 :  사용자명과 비밀번호가 정확한지 검증
            login(request, user)    # 로그인 : (위에 검증된)사용자 세션 생성
            return redirect('index')
    else:       # GET로 요청 시 회원가입 폼으로 이동
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


