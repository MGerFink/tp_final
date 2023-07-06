from django.contrib import admin

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
