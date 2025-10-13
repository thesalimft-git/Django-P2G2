from django.contrib import admin
from .models import Product, Order , OrderItem,Category

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','amount','created_at']
    ordering = ['id']
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','stock']
    list_editable = ['price']
    list_filter = ['name','price']
    
    ordering = ['id']

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Category)

# Register your models here.
