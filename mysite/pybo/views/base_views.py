#  기본관리 함수 파일 (index, detail)


from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404  # render : 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수

from ..models import Question  # model 중 Question, Answer 모델 사용
from django.db.models import Q


def index(request):
    page = request.GET.get('page', '1')  # 페이지 : http://localhost:8000/pybo/?page=1 처럼 GET 방식으로 호출된 URL에서 page값을 가져올 때 사용하는데 메인페이지로 호출됫을 시 기본값으로 page를 1로 설정
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')  # order_by() : 조회 결과를 정렬하는 함수, -가 있으면 역방향/없으면 순방향
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)  # 요청된 페이지에 해당되는 페이징 객체 생성 -> 페이징 객체에는 다양한 속성 존재(블로그 참고)
    last_page_num = 0
    for last_page in paginator.page_range:
        last_page_num = last_page
    context = {
        'question_list': page_obj,  # question_list는 페이징 객체
        'last_page_num': last_page_num,  # 마지막 페이지
        'page': page, 'kw': kw,
    }
    return render(request, 'pybo/question_list.html', context)  # 조회된 질문목록을 pybo/question_list.html 템플릿 파일로 리턴하여 응답


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 불러오는 Question모델의 기본키(PK)에 해당하는 값
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
