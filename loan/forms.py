from django import forms
from loan.models import Loan
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoanForm(forms.ModelForm):

    borrower = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Loan
        fields = ("borrower", "amount", "period", "reason", "applied_date")

    def clean_amount(self):
        if self.cleaned_data["amount"] <10000 or self.cleaned_data["amount"] >100000:
            raise ValidationError("The field is only allowed between [10000, 100000]!")
        else:
            return self.cleaned_data["amount"]
