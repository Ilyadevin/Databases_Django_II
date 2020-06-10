from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=25, default=1)
    tag = models.ManyToManyField(Article, through='PublishedArticles', verbose_name='Теги')

    def __str__(self):
        return self.name


class PublishedArticles(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False,
                                  verbose_name='Главный тег'
                                  )
