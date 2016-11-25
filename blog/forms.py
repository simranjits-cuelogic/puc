from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea)
    # is_published = forms.BooleanField(
    #     required=False,
    #     initial=True,
    #     label='Published?'
    #     )
