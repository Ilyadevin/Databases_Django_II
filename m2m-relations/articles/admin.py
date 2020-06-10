from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, PublishedArticles


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
        return super().clean()


class PublishedArticlesInline(admin.TabularInline):
    model = PublishedArticles
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PublishedArticlesInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [PublishedArticlesInline]
