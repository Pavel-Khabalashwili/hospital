# Generated by Django 4.2.7 on 2024-01-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_applications_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Cтатус'),
        ),
    ]
