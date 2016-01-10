from django import forms
from django.contrib.auth.models import User
from borrower.models import Borrower, BorrowerBusinesses
from django.core.exceptions import ValidationError
import re


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', "first_name", "last_name")


class BorrowerForm(forms.Form):

    telephone_number = forms.CharField(label="Telephone number:", max_length=11)

    def clean_telephone_number(self):
        match_group = re.search("^[0-9]+$", self.cleaned_data["telephone_number"])
        if match_group is None:
            raise ValidationError("The field is only allowed with [0-9]!")
        else:
            return self.cleaned_data["telephone_number"]


class BorrowerBusinessForm(forms.ModelForm):

    borrower = forms.ModelChoiceField(queryset=Borrower.objects.all(), widget=forms.HiddenInput())

    def clean_registered_number(self):
        match_group = re.search("^[0-9]+$", self.cleaned_data["registered_number"])
        if match_group is None:
            raise ValidationError("The field is only allowed with [0-9]!")
        else:
            return self.cleaned_data["registered_number"]

    class Meta:
        model = BorrowerBusinesses
        fields = ['borrower', 'name', 'address', 'registered_number', 'sector']

