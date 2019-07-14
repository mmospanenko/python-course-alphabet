from django.db import models
from account.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.title
