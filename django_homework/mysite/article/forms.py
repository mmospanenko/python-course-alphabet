from django import forms
from article.models import Article, Comments


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'description')
        labels = {
            'title': 'Custom Title',
        }


class CommentsForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    # object_id = forms.CharField()
    # model_name = forms.CharField()

    # class Meta:
    #     model = Comments
    #     fields = ('comment', )
    #     labels = {
    #         'comment': 'Add comment to article '
    #     }
