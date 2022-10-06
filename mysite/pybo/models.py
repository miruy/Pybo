from django.db import models

# Create your models here. DB에 필요한 model 생성, ORM으로 간편하게 사용가능

class Question(models.Model):   # 질문 클래스 생성
    subject = models.CharField(max_length=200)  # 제목 컬럼, 글자수 길이 제한이 필요한 속성은 CharField()사용
    content = models.TextField()    # 내용 컬럼, 글자수 길이 제한 필요없는 속성은 TextField()사용
    create_date = models.DateTimeField()    # 작성일

    def __str__(self):
        return self.subject

class Answer(models.Model): # 답변 클래스 생성
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 질문의 대한 답변이므로 Question클래스(테이블)을 참조해야함, 질문과 답변이 이어진 데이터가 삭제될 경우 함께 삭제(하나의 질문에 많은 답변이 달릴 수 있으므로)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content



