from django.db import models

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=100)
    name.primary_key = True
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    name.primary_key = True
    contenu = models.TextField(null=True)
    categorie = models.ForeignKey('Categorie')
    def __str__(self):
        return self.name

class Shop(models.Model):
    id_shop = models.IntegerField()
    id_shop.primary_key = True
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product', through='Offer')
    def __str__(self):
        return self.name

class Offer(models.Model):
    id_offer = models.IntegerField()
    id_offer.primary_key = True
    price = models.IntegerField()
    product = models.ForeignKey('Product')
    shop = models.ForeignKey('Shop')
    def __str__(self):
        return "{0} sold by {1} at price of {2} e ".format(self.product, self.shop, self.price)
