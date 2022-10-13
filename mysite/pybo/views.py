from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect # render : 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
from .models import Question    # model 중 Question 모델 사용
from django.utils import timezone
# from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    page = request.GET.get('page', '1')     # 페이지 : http://localhost:8000/pybo/?page=1 처럼 GET 방식으로 호출된 URL에서 page값을 가져올 때 사용하는데 메인페이지로 호출됫을 시 기본값으로 page를 1로 설정
    question_list = Question.objects.order_by('-create_date')   # order_by() : 조회 결과를 정렬하는 함수, -가 있으면 역방향/없으면 순방향
    paginator = Paginator(question_list, 10)    # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)  # 요청된 페이지에 해당되는 페이징 객체 생성 -> 페이징 객체에는 다양한 속성 존재(블로그 참고)
    last_page_num = 0
    for last_page in paginator.page_range:
        last_page_num = last_page
    context = {
        'question_list': page_obj,      # question_list는 페이징 객체
        'last_page_num': last_page_num,   # 마지막 페이지
    }
    return render(request, 'pybo/question_list.html', context) # 조회된 질문목록을 pybo/question_list.html 템플릿 파일로 리턴하여 응답


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 불러오는 Question모델의 기본키(PK)에 해당하는 값
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')      # 로그인이 필요한 함수라는 것을 정의
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user    # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
        # return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')       # 로그인이 필요한 함수라는 것을 정의
def question_create(request):   # 질문 등록 메서드
    if request.method == 'POST':    # post로 요청이 왔다면
        form = QuestionForm(request.POST)   # 요청이 온 객체를 form이라는 변수에 대입
        if form.is_valid():   # 요청이 온 객체가 데이터를 가지고 있다면(질문제목과 내용이 있다면)
            question = form.save(commit=False)  # 질문제목, 내용 데이터 임시 저장(아직 DB에는 저장안함)
            question.author = request.user      # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()   # 작성일 저장
            question.save()  # 데이터를 실제로 객체에 저장(실제 DB에 데이터 저장)
            return redirect('pybo:index')   # 성공 후 질문 목록페이지로 리턴
    else:      # get으로 왔다면(post로 요청이 오지 않았다면)
        form = QuestionForm()   # 빈 객체를 form 변수에 대입(질문제목과 내용없음)
    context = {'form': form}    # 질문 등록 페이지로 리턴
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:     # 로그인된 유저와 질문을 등록한 유저가 같지 않다면
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":    # 로그인된 유저와 질문을 등록한 유저가 같을 때 POST로 요청이 들어왔다면 수정기능 실행
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():     # 수정폼에 입력된 값이 있다면 저장
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:        # 로그인된 유저와 질문을 등록한 유저가 같을 때 GET으로 요청이 들어왔다면 수정폼 보여주기
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

