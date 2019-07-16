from django.db import models
from account.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    comment = RichTextUploadingField(null=True, blank=True)
    date = models.DateTimeField(
        'Date of adding a comment', auto_now_add=True, null=True
    )
    moderation = models.BooleanField('moderation', default=False)

    def __str__(self):
        return "{}".format(self.author)
