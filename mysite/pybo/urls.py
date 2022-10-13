from django.urls import path
from .views import base_views, question_views, answer_views

app_name = 'pybo'

# views.index -> base_views.index 변경

urlpatterns = [

    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),

    # path('', views.index, name='index'),  # /pybo로 url요청 시 views.index로 리턴
    # path('<int:question_id>/', views.detail, name='detail'), # int 형의 question_id가(= /pybo/2 )로 url요청 시 views.detail로 리턴
    # path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), # 답변 등록 기능 경로, 메서드, 별칭
    # path('question/create/', views.question_create, name='question_create'),    # 질문 등록 기능 추가(경로, 메서드, 별칭)
    # path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    # path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
