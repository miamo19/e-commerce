from django.db import models

# Create your models here.
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

"""
Product
-Nom
-Prix
-la quantite en stock
-Desccription
-Image

"""

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('products', kwargs={"slug": self.slug})

# Article (Order)
"""
-produit
-quantite
-commande ou non
"""
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.product.name} ({self.quantity})"


# Panier (Cart)
"""
-utilisateur
-Articles
-Commande ou non
-Date de la commande
"""
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username