from django import forms
from .models import Article

from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'rows':30}))

    class Meta:
        model = Article
        fields = ['title', 'desription', 'content', 'image']
