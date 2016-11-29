from django import forms
from .models import Article, Comment

from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'rows':30}))

    class Meta:
        model = Article
        fields = ['title', 'desription', 'content', 'image']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=100)
    class Meta:
        model = Comment
        fields = ['comment']
