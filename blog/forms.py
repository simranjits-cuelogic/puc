from django import forms
from .models import Article

from djrichtextfield.widgets import RichTextWidget

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=RichTextWidget())

    class Meta:
        model = Article
        fields = ['title', 'content']
