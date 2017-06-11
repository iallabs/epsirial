from django.contrib import admin
from . import models
# Register your models here.
models =(models.Product, models.Categorie, models.Shop, models.Offer)
for m in models:
    admin.site.register(m)
