from django.db import models


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Retailer(models.Model):
    name = models.CharField(max_length=255)
    vendors = models.ManyToManyField("Vendor")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Briefing(models.Model):
    name = models.CharField(max_length=255)
    retailer = models.ForeignKey(
        "Retailer",
        on_delete=models.CASCADE,
    )
    responsible = models.CharField(max_length=255)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
    )
    release_date = models.DateField()
    available = models.IntegerField()

    def __str__(self):
        return self.name
