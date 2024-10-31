from django.db import models
from .price import Price
from .product_type import ProductType


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название товара"
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        verbose_name="Цена"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество"
    )
    barcode = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Штрихкод"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        verbose_name="Тип товара"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"