from django import forms
from articles.models import Article

# # 유효성 검사 함수를 필요로 할 때
# # 입력한 문자가 숫자로만 이루어진 경우에는 에러를 발생
# # forms.Va;idationError - 이 에러를 발생
# def is_not_digit_string_validator(value):
#     if value.isdigit():
#         raise forms.ValidationError(" 이 문자는 숫자로만 이루어져 있어요!")

# # Model Fields : 데이터베이스 필드들을 파이썬 클래스화
# # Form Fields : HTML FORM .Field(element)들을 파이썬 클래스화
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10, validators=[is_not_digit_string_validator])
#     content = forms.CharField(widget=forms.Textarea(
#         attrs= {
#             'cols':20,
#             'rows':5,
#             'class':'content-area'
#         }
#     ))
#     # email = forms.CharField(widget=forms.EmailInput)
#     # password = forms.CharField(widget=forms.PasswordInput)
    
#     def save(self):
#         article = Article(**self.cleaned_data) # 키워드 인자형태로 넘김
#         article.save()
#         return article


class ArticleForm(forms.Form):
    class Meta:
        model = Article
        fields = "__all__"
        