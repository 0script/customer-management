from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.EmailField( max_length=254,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name=models.CharField( max_length=50,null=True)
    price=models.DecimalField( max_digits=5, decimal_places=2,null=True)
    tags=models.ForeignKey(Tag,null=True,on_delete=models.SET_NULL)
    category=models.CharField( max_length=50,null=True,choices=CATEGORY)
    description=models.CharField( max_length=250,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    #dropdown menu for status
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    #one to many relationship
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField( max_length=50,choices=STATUS)

    def __str__(self):
        return self.product.name
