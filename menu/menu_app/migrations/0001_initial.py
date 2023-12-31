# Generated by Django 4.2.6 on 2023-10-31 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('url', models.CharField(blank=True, max_length=200, verbose_name='Ссылка')),
                ('position', models.PositiveIntegerField(default=1, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'ordering': ('position',),
            },
        ),
    ]
