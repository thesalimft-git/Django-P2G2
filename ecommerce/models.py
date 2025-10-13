from django.db import models

import uuid


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null= True ,blank=True)
    image = models.ImageField(upload_to='products',null= True ,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    category =models.ForeignKey('Category',on_delete=models.PROTECT,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # rating = models.IntegerField(validators=[MinLengthValidator(1),MaxValueValidator(5)], default=0)
    
    def __str__(self):
        
        return f"{self.name} ({self.price})"
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name



class Order(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    STATUS_CHOICES = (
        ('paid','paid'),
        ('pending','pending'),
        ('cancelled','cancelled')
    )
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.uuid)
    
   
    
class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.PROTECT,related_name='order_items')
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
    
    
    

    
 
 
    