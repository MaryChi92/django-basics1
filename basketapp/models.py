from django.db import models
from django.conf import settings

from mainapp.models import Product


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')

    def __str__(self):
        return f'{self.product}, {self.quantity}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('created_at',)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        # return sum(list(map(lambda x: x.quantity, _items)))
        return sum(list(_items.values_list('quantity', flat=True)))

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.product_cost, _items)))

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity

        self.product.save()
        super().save(*args, **kwargs)
