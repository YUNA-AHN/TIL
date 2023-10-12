from django import forms
from .models import Review

class ReviewFrom(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)