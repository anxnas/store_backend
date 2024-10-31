from django.db import models


class Price(models.Model):
    currency = models.CharField(
        max_length=3,
        verbose_name="Валюта"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость"
    )

    def __str__(self):
        return f"{self.amount} {self.currency}"

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"