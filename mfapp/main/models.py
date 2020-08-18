from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)  # до 50 символов
    task = models.TextField('Описание')  # много символов

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'