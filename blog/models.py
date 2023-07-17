from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=90, help_text='Название')
    text = models.TextField(help_text='Текст новости')
    time_create = models.DateTimeField(auto_now_add=True, help_text='Время создания новости')
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Автор новости')

    class Meta:
        verbose_name = 'Новость'

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE, help_text='Новость на которую оставили комментарий')
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Автор комментария')
    text = models.TextField(max_length=450, help_text='Текст комментария')
    time_create = models.DateTimeField(auto_now_add=True, help_text='Время создания комментария')

    class Meta:
        verbose_name = 'Комментарий'


class Like(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE, help_text='Новость на котрую поставили лайк')
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Автор лайка')
    time_create = models.DateTimeField(auto_now_add=True, help_text='Время создания лайка')

    class Meta:
        verbose_name = 'Лайк'
