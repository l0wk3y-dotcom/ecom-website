from django.contrib import admin
from .models import Category, Product, ProductImage, Color, Size
# Register your models here.

admin.site.register(Category)
class ProductImage(admin.StackedInline):
    model=ProductImage

class ImageField(admin.ModelAdmin):
    list_display=["product_name", "price", "category"]
    inlines=[ProductImage]

admin.site.register(Product, ImageField)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display=['color_name','price']
    model=Color

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display=['size_name','price']
    model=Size
