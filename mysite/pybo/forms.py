# form : 페이지 요청 시 전달되는 파라미터들을 쉽게 관리하기 위해 사용하는 클래스
# !질문 등록 시 반복적으로 사용할 질문 폼 따로 작성


from django import forms    # 폼 클래스 사용
from pybo.models import Question


# 장고의 폼은 일반 폼(forms.Form) / 모델 폼(forms.ModelForm)로 나누어짐

# QuestionForm 메서드는 Question 모델과 연결된 폼이고, subject(질문 제목), content(질문 내용)를 속성으로 가진다.

class QuestionForm(forms.ModelForm):    # 모델 폼(forms.ModelForm) : 모델과 연결된 폼이므로 폼을 저장하면 연결된 모델의 데이터를 저장할 수 있음
    class Meta:            # 모델 폼은 이너클래스인 Meta클래스를 꼭! 함께 사용해야함
        model = Question    # 사용할 모델
        fields = ['subject', 'content']     # 사용할 속성(필드)

