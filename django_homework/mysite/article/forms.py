from django import forms
from article.models import Article


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(max_length=5)

    class Meta:
        model = Article
        fields = ('title', 'description')
        labels = {
            'title': 'Custom Title',
        }
