from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25, default=1)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tag = models.ManyToManyField(Tag, through='PublishedArticles', through_fields=('article', 'tags'),
                                 verbose_name='Теги')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class PublishedArticles(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статьи')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Теги')
    is_main = models.BooleanField(default=False, verbose_name='Главный тег')
