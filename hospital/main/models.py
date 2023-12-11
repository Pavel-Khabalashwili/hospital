from django.db import models
from django.contrib.auth.models import AbstractUser


class Applications(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    desk  = models.TextField('Описание')
    status = models.CharField('Cтатус', max_length=200)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
