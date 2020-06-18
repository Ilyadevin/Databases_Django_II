from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, PublishedArticles
from collections import Counter


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        bool_counter = 0
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main'] is True:
                    bool_counter += 1
                elif bool_counter == 1:
                    return super().clean()
                elif bool_counter > 1:
                    raise ValidationError('Главный тег уже есть')
                elif bool_counter == 0:
                    raise ValidationError('Нужно указать один главный тег')


class PublishedArticlesInline(admin.TabularInline):
    model = PublishedArticles
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PublishedArticlesInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [PublishedArticlesInline]
