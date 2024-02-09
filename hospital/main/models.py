from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
import os


class Applications(models.Model):
    STATUS_CHOICES = (
        (0, 'Не готово'),
        (1, 'В работе'),
        (2, 'Готово'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=50)
    desk = models.TextField('Описание')
    status = models.IntegerField('Статус', choices=STATUS_CHOICES, default=0)
    image = models.ImageField('Изображение', upload_to='photos/', null=True, blank=True)
    datetime_field = models.DateTimeField("Дата - время", default=timezone.now)

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