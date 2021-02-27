from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    content = models.TextField(max_length=3000, null=False, blank=False)
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.id}. {self.author}: {self.title}'