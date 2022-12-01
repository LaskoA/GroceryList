from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=63, unique=True)

    def clean(self):
        self.title = self.title.lower()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def clean(self):
        self.name = self.name.lower()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "products"
        ordering = ["name"]


class Purchase(models.Model):
    products = models.OneToOneField(Product, on_delete=models.CASCADE, unique=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    status = models.BooleanField()
    quantity = models.CharField(max_length=63, blank=True, null=True)
    scale = models.CharField(max_length=63, blank=True, null=True)
    comment = models.CharField(max_length=63, blank=True, null=True)

    class Meta:
        ordering = ["status", "products__name"]

    def __str__(self):
        return self.products.name
