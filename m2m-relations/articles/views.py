from django.shortcuts import render
from .models import Article, PublishedArticles


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = PublishedArticles.objects.all().order_by(ordering)
    context = {'object_list': PublishedArticles,}
    return render(request, template, context)
