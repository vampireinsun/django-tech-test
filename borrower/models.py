from django.contrib.auth.models import User
from django.db import models


class Borrower(models.Model):

    user = models.OneToOneField(User)

    telephone_number = models.CharField(max_length=11, null=True)


class BorrowerBusinesses(models.Model):
    SECTOR_CHOICES = (
        ('RETAIL', 'Retail'),
        ('PRO_SERVICE', 'Professional Services'),
        ('FOOD_DRINK', 'Food & Drink'),
        ('ENTERTAINMENT', 'Entertainment'),
    )

    borrower = models.ForeignKey(Borrower)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=250, null=False)
    registered_number = models.CharField(max_length=8, null=False)
    sector = models.CharField(max_length=20, null=False, choices=SECTOR_CHOICES)
