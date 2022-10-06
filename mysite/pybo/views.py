from django.shortcuts import render

# Create your views here.
from django.shortcuts import render # render : 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
from .models import Question    # model 중 Question 모델 사용


def index(request):
    question_list = Question.objects.order_by('-create_date')   # order_by() : 조회 결과를 정렬하는 함수, -가 있으면 역방향/없으면 순방향
    context = {'question_list' : question_list} #
    return render(request, 'pybo/question_list.html', context) # 조회된 질문목록을 pybo/question_list.html 템플릿 파일로 리턴하여 응답