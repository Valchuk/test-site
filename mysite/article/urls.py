from django.urls import path, re_path
from django.views.generic import ListView
from article.models import Article
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.basic_one, name='basic_one'),
    path('home/', ListView.as_view(queryset = Article.objects.all().order_by('-article_date')[:5], template_name='news/posts.html')),
    path('home/<int:article_id>/', views.article, name='article'),
    path('archive/', views.archive, name='archive'),
    path('contact/', views.contact, name='contact'),
    path('archive/addlike/<int:article_id>/', views.addlike, name='addlike'),
    path('home/addcomment/<int:article_id>/', views.addcomment, name='addcomment'),
    re_path(r'page=(\d+)', views.archive, name='archive'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
