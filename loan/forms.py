from django import forms
from loan.models import Loan
from django.contrib.auth.models import User


class LoanForm(forms.ModelForm):

    borrower = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Loan
        fields = ("borrower", "amount", "period", "reason", "applied_date")
