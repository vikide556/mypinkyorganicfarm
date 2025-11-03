from django.contrib import admin
from .models import MyfarmProduct,ProductCategory

class MyfarmProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

    



admin.site.register(MyfarmProduct,MyfarmProductAdmin)
admin.site.register(ProductCategory,ProductCategoryAdmin)