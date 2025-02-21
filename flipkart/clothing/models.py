from django.db import models

# Create your models here.
class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    ]

    COLOUR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Black', 'Black'),
        ('White', 'White')
    ]

    name = models.CharField(max_length=200)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    colour = models.CharField(max_length=10, choices=COLOUR_CHOICES, default='Red')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_img/')

def __str__(self):
        return self.name 
