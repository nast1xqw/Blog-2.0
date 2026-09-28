from django.db import models

class Post(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=128,
    )
    text = models.TextField(
        verbose_name='Текст',
        max_length=512,
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    ) 
    author = models.ForeignKey(
        to='users.User',
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'