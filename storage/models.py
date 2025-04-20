from django.db import models

class Product(models.Model):
    barcode = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    expiration_date = models.DateField()

    def __str__(self):
        return f'{self.name} ({self.barcode})'
