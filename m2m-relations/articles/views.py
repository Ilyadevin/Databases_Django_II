from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all().order_by(ordering)
    published=Tag.objects.all()
    print(published)
    context = {'object_list': articles}
    return render(request, template, context)
