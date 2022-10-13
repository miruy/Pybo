import markdown
from django import template
from django.utils.safestring import  mark_safe

register = template.Library()


# 템플릿 필터 함수 만들기


@register.filter  # 해당 함수를 템플릿 필터 함수로 사용하겠다는 어노테이션
def sub(value, arg):
    return value - arg


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))