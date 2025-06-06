from django.shortcuts import render
from . import models
from datetime import datetime

def posts(request, **kwargs):
    print(request.GET)
    my_posts = models.Article.objects.filter(
        user=kwargs['uid']  # request.GET.get('uid')
    )
    # __gt > greater than
    # __lt < less than
    # __gte >= greater than or equal
    # __lte <=

    context = {
        'author': 'Я',
        'uid': str(kwargs['uid']), # request.GET.get('uid'),
        'all_posts': my_posts
        # получить из БД ВСЕ объекты art
    }
    return render(
        request,
        'article/feed.html',
        context
    )

from . import forms
def publish(request):
    print(request.GET)
    context = {
        'new_blog_post_form': 
            forms.BlogPostForm()
    }
    if request.GET:
        models.Article(
            title=request.GET['header'],
            text=request.GET['text'],
        ).save()
    return render(
        request,
        'article/new.html',
        context)
