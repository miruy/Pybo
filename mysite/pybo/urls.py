from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),  # /pybo로 url요청 시 views.index로 리턴
    path('<int:question_id>/', views.detail, name='detail'), # int 형의 question_id가(= /pybo/2 )로 url요청 시 views.detail로 리턴
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), # 답변 등록 기능 경로, 메서드, 별칭
    path('question/create/', views.question_create, name='question_create'),    # 질문 등록 기능 추가(경로, 메서드, 별칭)
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
]