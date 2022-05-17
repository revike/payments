from django.core.exceptions import ValidationError
from django.db import models


class Item(models.Model):
    """Model for Item"""

    class Meta:
        verbose_name_plural = 'продукты'
        verbose_name = 'продукты'

    name = models.CharField(max_length=128, verbose_name='название')
    description = models.CharField(max_length=512, verbose_name='описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0,
                                blank=False, verbose_name='цена')

    def clean(self):
        if self.price < 40:
            raise ValidationError(message='Price must be over 40',
                                  code='Invalid')

    def __str__(self):
        return f'{self.name}'
