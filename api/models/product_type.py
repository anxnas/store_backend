from django.db import models


class ProductType(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название типа"
    )
    description = models.TextField(
        verbose_name="Описание типа"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип товара"
        verbose_name_plural = "Типы товаров"