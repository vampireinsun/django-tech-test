from django.contrib import admin
from django import forms
from borrower.models import Borrower, BorrowerBusinesses
from django.core.exceptions import ValidationError
import re


class BorrowerAdminForm(forms.ModelForm):

    def clean_telephone_number(self):
        match_group = re.search("^[0-9]+$", self.cleaned_data["telephone_number"])
        if match_group is None:
            raise ValidationError("The field is only allowed with [0-9]!")
        else:
            return self.cleaned_data["telephone_number"]


class BorrowerBusinessInLineFormset(forms.models.BaseInlineFormSet):

    def clean(self):
        super(BorrowerBusinessInLineFormset, self).clean()
        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                match_group = re.search("^[0-9]+$", form.cleaned_data["registered_number"])
                if match_group is None:
                    raise ValidationError("The field: registered number is only allowed with [0-9]!")


class BorrowerBusinessAdminForm(admin.TabularInline):
    model = BorrowerBusinesses
    extra = 3
    formset = BorrowerBusinessInLineFormset


class BorrowerAdmin(admin.ModelAdmin):

    list_display = ("user", "telephone_number")
    inlines = [BorrowerBusinessAdminForm]

    form = BorrowerAdminForm

admin.site.register(Borrower, BorrowerAdmin)
