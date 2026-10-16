from django.contrib import admin
from products.models import Category,Product,Color_temperature,Effectiveness

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}

@admin.register(Color_temperature)
class Color_temperatureAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}

@admin.register(Effectiveness)
class EffectivenessAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}


