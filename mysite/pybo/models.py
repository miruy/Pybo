from django.db import models
from django.contrib.auth.models import User


# Create your models here. DB에 필요한 model 생성, ORM으로 간편하게 사용가능


class Question(models.Model):  # 질문 클래스 생성
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_question')  # relate_name : 인수를 지정하여 voter와 헷갈리지 않게 정리
    subject = models.CharField(max_length=200)  # 제목 컬럼, 글자수 길이 제한이 필요한 속성은 CharField()사용
    content = models.TextField()  # 내용 컬럼, 글자수 길이 제한 필요없는 속성은 TextField()사용
    create_date = models.DateTimeField()  # 작성일
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정일, null 허용, 입력된 데이터 검증 시 값 없어도 됨
    voter = models.ManyToManyField(User,
                                   related_name='voter_question')  # 추천인(좋아요)추가 , ManyToManyField : 다대다 관계(질문:좋아요), relate_name : 인수를 지정하여 author와 헷갈리지 않게 정리

    def __str__(self):
        return self.subject


class Answer(models.Model):  # 답변 클래스 생성
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)  # 질문의 대한 답변이므로 Question클래스(테이블)을 참조해야함, 질문과 답변이 이어진 데이터가 삭제될 경우 함께 삭제(하나의 질문에 많은 답변이 달릴 수 있으므로)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정일, null 허용, 입력된 데이터 검증 시 값 없어도 됨
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content
