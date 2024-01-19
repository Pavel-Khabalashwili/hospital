from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import os


class Applications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=50)
    desk  = models.TextField('Описание')
    status = models.BooleanField('Cтатус', default=False)
    image = models.ImageField(upload_to='photos/', null=True, blank=True, )

    def delete(self, *args, **kwargs):
        # Сначала удаляем файл изображения
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        # Затем вызываем метод delete родительского класса
        super(Applications, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
