# Generated by Django 5.0.3 on 2024-03-25 11:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_timeslot_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время окончания'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='time_slots/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='is_realtime',
            field=models.BooleanField(default=False, verbose_name='В реальном времени'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время начала'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='tags',
            field=models.ManyToManyField(to='web.timeslottag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='timeslottag',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='timeslottag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
