from django.db import models
from django.contrib.auth.models import User


class Loan(models.Model):

    LOAD_STATUS = (
        ("u", "Under Review"),
        ("a", "Approved"),
        ("r", "Rejected"),
    )

    borrower = models.ForeignKey(User)
    amount = models.IntegerField(null=False)
    period = models.IntegerField(null=False)
    reason = models.TextField(null=False)
    status = models.CharField(max_length=1, null=False, default="u", choices=LOAD_STATUS)
    applied_date = models.DateTimeField(null=False)


class RepaymentHistory(models.Model):

    loan = models.ForeignKey(Loan)
    amount = models.IntegerField(null=False)
    timestamp = models.DateTimeField(null=False)
