from django.db import models


class Tshirt(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=150, null=False)
    size = models.CharField(max_length=3, null=False)
    quantity = models.PositiveSmallIntegerField(null=False)