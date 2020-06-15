from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, PublishedArticles
from collections import Counter


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        bool_counter = Counter()
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main'] is False and bool_counter[form.cleaned_data['is_main']] == 0:
                    raise ValidationError('У статьи должен быть главный тег!')
                elif form.cleaned_data['is_main'] is True and bool_counter[form.cleaned_data['is_main']] == 1:
                    return super().clean()
                elif form.cleaned_data['is_main'] is True and bool_counter[form.cleaned_data['is_main']] > 1:
                    raise ValidationError('Главный тег уже сть')
            else:
                raise ValidationError('Тег не может быть пустым!')


class PublishedArticlesInline(admin.TabularInline):
    model = PublishedArticles
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PublishedArticlesInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [PublishedArticlesInline]
