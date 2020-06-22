from django.shortcuts import render
from .models import Article, PublishedArticles


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all()
    tags = PublishedArticles.objects.all()
    context = {'object_list': articles, 'tags': tags}
    return render(request, template, context)
