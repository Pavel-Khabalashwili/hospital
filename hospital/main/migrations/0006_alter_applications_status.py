# Generated by Django 4.2.7 on 2024-02-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_applications_datetime_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Статус'),
        ),
    ]
