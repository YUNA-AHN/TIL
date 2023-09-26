from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget = forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder': 'Enter the title',
                'maxlength':10,
            }
        ),
    )
    content =  forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder': 'Enter the content',
                'rows':5,
                'cols': 50,
                }
        ),
        error_messages = {'required' : '내용을 입력해주세요.'},
    )
    # 모델을 등록
    class Meta:
        model = Article
        fields = '__all__' 
        # fields = ('title',) # 내가 출력하고자 하는 컬럼 지정하는 방식
        # exclude = ('title', ) # 제외하는 방식