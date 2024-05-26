from django.db import models


STR_LIMIT = 50


class Category(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=200, verbose_name="URL", unique=True, blank=True, null=True
    )

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name[:STR_LIMIT]


class Product(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=200, verbose_name="URL", unique=True, blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Описание", null=True, blank=True
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="goods_images",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        verbose_name="Цена", default=0.00, max_digits=7, decimal_places=2
    )
    discount = models.DecimalField(
        verbose_name="Скидка в %", default=0.00, max_digits=4, decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество", default=0
    )
    category = models.ForeignKey(
        verbose_name="Категория", to=Category, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)

    def __str__(self) -> str:
        return self.name[:STR_LIMIT]

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - ((self.price * self.discount) / 100), 2)
        return self.price
