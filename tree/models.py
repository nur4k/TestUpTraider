from django.db import models


class Tree(models.Model):
    branch = models.CharField(verbose_name='Ветка', max_length=100)
    category = models.CharField(verbose_name='Категория', max_length=100)
    sub_category = models.CharField(verbose_name='Суб категория', max_length=100)

    class Meta:
        verbose_name = 'Дерево'
        verbose_name_plural = 'Деревья'

    def __str__(self) -> str:
        return self.branch