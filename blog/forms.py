from django import forms
from .models import Article, Comment

from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'rows':30}))

    class Meta:
        model = Article
        fields = ['title', 'desription', 'content', 'image']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'rows':5,
                'style':'resize:none;'
                }
            )
        )
    class Meta:
        model = Comment
        fields = ['comment', 'article', 'user']
        widgets = {
        'article': forms.HiddenInput(),
        'user': forms.HiddenInput()
        }
