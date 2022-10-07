from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),  # /pybo로 url요청 시 views.index로 리턴
    path('<int:question_id>/', views.detail, name='detail'), # int 형의 question_id가(= /pybo/2 )로 url요청 시 views.detail로 리턴
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), # 기능안의 세부 기능(앱 안의 새부 앱)의 경로, 메서드, 별칭
]