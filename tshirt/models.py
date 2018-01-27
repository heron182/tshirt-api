from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=150, null=False)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Tshirt(models.Model):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'
    SIZE_CHOICES = ((SMALL, 'S'), (MEDIUM, 'M'), (LARGE, 'L'), (EXTRA_LARGE,
                                                                'XL'))
    name = models.CharField(max_length=150, null=False)
    brand = models.ForeignKey(
        Brand, related_name='tshirts', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='tshirts', on_delete=models.CASCADE)
    color = models.ForeignKey(
        Color, related_name='tshirts', on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    quantity = models.PositiveSmallIntegerField(null=False)
    unity_price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', )
