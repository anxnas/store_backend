from django.contrib import admin
from .models import Product, ProductType, Price

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'barcode', 'updated_at', 'product_type')
    search_fields = ('name', 'barcode')
    list_filter = ('product_type',)

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('amount', 'currency')
    list_filter = ('currency',)