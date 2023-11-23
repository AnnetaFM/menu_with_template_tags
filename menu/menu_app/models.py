from django.db import models


class Menu(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Родителький элемент'
        )
    url = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Ссылка',
        )
    named_url = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Именованная ссылка',
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
