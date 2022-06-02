"""Import"""
from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """Product display"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'colour',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Category display"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'review', 'review_author', 'product')


admin.site.register(Review, ReviewAdmin)
