#  질문 관리 함수 파일 (question_create, question_modify, question_delete)

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect  # render : 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question  # model 중 Question, Answer 모델 사용


@login_required(login_url='common:login')  # 로그인이 필요한 함수라는 것을 정의
def question_create(request):  # 질문 등록 메서드
    if request.method == 'POST':  # post로 요청이 왔다면
        form = QuestionForm(request.POST)  # 요청이 온 객체를 form이라는 변수에 대입
        if form.is_valid():  # 요청이 온 객체가 데이터를 가지고 있다면(질문제목과 내용이 있다면)
            question = form.save(commit=False)  # 질문제목, 내용 데이터 임시 저장(아직 DB에는 저장안함)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()  # 작성일 저장
            question.save()  # 데이터를 실제로 객체에 저장(실제 DB에 데이터 저장)
            return redirect('pybo:index')  # 성공 후 질문 목록페이지로 리턴
    else:  # get으로 왔다면(post로 요청이 오지 않았다면)
        form = QuestionForm()  # 빈 객체를 form 변수에 대입(질문제목과 내용없음)
    context = {'form': form}  # 질문 등록 페이지로 리턴
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:  # 로그인된 유저와 질문을 등록한 유저가 같지 않다면
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":  # 로그인된 유저와 질문을 등록한 유저가 같을 때 POST로 요청이 들어왔다면 수정기능 실행
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():  # 수정폼에 입력된 값이 있다면 저장
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:  # 로그인된 유저와 질문을 등록한 유저가 같을 때 GET으로 요청이 들어왔다면 수정폼 보여주기
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:  # 로그인된 유저와 질문을 등록한 유저가 같지 않다면
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()  # 로그인된 유저와 질문을 등록한 유저가 같다면 질문삭제 실행
    return redirect('pybo:index')
