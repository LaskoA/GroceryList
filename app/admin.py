from django.contrib import admin
from app.models import Purchase, Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, ProductAdmin)

admin.site.register(Purchase)
admin.site.register(Category)
