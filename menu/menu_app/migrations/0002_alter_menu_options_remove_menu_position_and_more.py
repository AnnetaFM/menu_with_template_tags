# Generated by Django 4.2.6 on 2023-11-01 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='position',
        ),
        migrations.AddField(
            model_name='menu',
            name='named_url',
            field=models.CharField(blank=True, max_length=100, verbose_name='Именованная ссылка'),
        ),
        migrations.AddField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_app.menu', verbose_name='Родителький элемент'),
        ),
    ]
