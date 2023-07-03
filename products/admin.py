from django.contrib import admin

from products.models import Product, ProductCategory, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'price', 'quantity', 'category',)
    search_fields = ('name',)
    readonly_fields = ('description',)
    fields = ('name', 'description',
              ('price', 'quantity'), 'image', 'category',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp',)
    readonly_fields = ('created_timestamp',)
    extra = 0
