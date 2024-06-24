from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    title = models.CharField('Задание', max_length=200)
    is_complete = models.BooleanField('Завершено', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"