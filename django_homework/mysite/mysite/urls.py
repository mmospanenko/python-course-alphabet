"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from account.views import ProfileDetailView, StartView, SignUp
from article.views import (
    IndexView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    CommentArticleCreate,
    CommentAddToComment
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(), name='index'),
    # Article
    path('article/create', ArticleCreateView.as_view(), name='create'),
    path(
        'article/<int:article_id>',
        ArticleDetailView.as_view(),
        name='detail'
    ),
    path(
        'article/update/<int:article_id>',
        ArticleUpdateView.as_view(),
        name='update'
    ),
    path(
        'article/delete/<int:article_id>',
        ArticleDeleteView.as_view(),
        name='delete'
    ),
    # Comment
    path(
        'comment/',
        CommentArticleCreate.as_view(),
        name='comment'
    ),
    path(
        'comment/<int:comment_id>',
        CommentAddToComment.as_view(),
        name='comment_add'
    ),
    # Account profile
    path(
        'account/profile/<int:profile_id>',
        ProfileDetailView.as_view(),
        name='profile'
    ),
    path('account/', include('django.contrib.auth.urls')),
    path('', StartView.as_view(), name='start'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
