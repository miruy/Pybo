from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect # render : 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
from .models import Question    # model 중 Question 모델 사용
from django.utils import timezone
from .forms import QuestionForm



def index(request):
    question_list = Question.objects.order_by('-create_date')   # order_by() : 조회 결과를 정렬하는 함수, -가 있으면 역방향/없으면 순방향
    context = {'question_list' : question_list} #
    return render(request, 'pybo/question_list.html', context) # 조회된 질문목록을 pybo/question_list.html 템플릿 파일로 리턴하여 응답


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 불러오는 Question모델의 기본키(PK)에 해당하는 값
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)


def question_create(request):   # 질문 등록 메서드
    if request.method == 'POST':    # post로 요청이 왔다면
        form = QuestionForm(request.POST)   # 요청이 온 객체를 form이라는 변수에 대입
        if form.is_valid():   # 요청이 온 객체가 데이터를 가지고 있다면(질문제목과 내용이 있다면)
            question = form.save(commit=False)  # 질문제목, 내용 데이터 임시 저장(아직 DB에는 저장안함)
            question.create_date = timezone.now()   # 작성일 저장
            question.save() # 데이터를 실제로 객체에 저장(실제 DB에 데이터 저장)
            return redirect('pybo:index')   # 성공 후 질문 목록페이지로 리턴
    else:      # get으로 왔다면(post로 요청이 오지 않았다면)
        form = QuestionForm()   # 빈 객체를 form 변수에 대입(질문제목과 내용없음)
    context = {'form': form}    # 질문 등록 페이지로 리턴
    return render(request, 'pybo/question_form.html', context)