from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, PublishedArticles
from collections import Counter

Bool_counter = Counter()


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    Bool_counter[form.cleaned_data['is_main']] += 1
                    if Bool_counter[form.cleaned_data['is_main']] > 1:
                        raise ValidationError('Главный тег')
                    else:
                        return super().clean()
                else:
                    return super().clean()
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
