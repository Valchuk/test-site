from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comment
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator

def basic_one(request):
    view = 'basic_one'
    return render(request, 'article/wrapper.html', {'name': view})

def contact(request):
    return render(request, 'article/basic.html', {'values':['Справка', '+380961122333']} )

def archive(request, page_number=1):
    all_articles = Article.objects.all().order_by('-article_date')
    current_page = Paginator(all_articles, 2)
    return render_to_response('news/posts.html', {'object_list':current_page.page(page_number), 'username':auth.get_user(request).username})

def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(comment_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('news/post.html', args)

def addlike(request, article_id):
    back_url = request.META['HTTP_REFERER']
    try:
        if article_id in request.COOKIES:
            redirect(back_url)
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect(back_url)
            response.set_cookie(str(article_id), 'value')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(back_url)

def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/home/%s/' % article_id)
