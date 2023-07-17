from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=90, help_text='Название')
    slug = models.SlugField(max_length=255, unique=True)
    text = models.TextField(help_text='Текст новости')
    time_create = models.DateTimeField(auto_now_add=True, help_text='Дата создания новости')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


