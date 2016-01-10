from django.contrib import admin
from loan.models import Loan, RepaymentHistory
from django.core.exceptions import ValidationError
from django import forms


class RepaymentHistoryAdminForm(admin.TabularInline):
    model = RepaymentHistory
    extra = 3

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class LoanAdminForm(forms.ModelForm):

    def clean_amount(self):
        if self.cleaned_data["amount"] <10000 or self.cleaned_data["amount"] >100000:
            raise ValidationError("The field is only allowed between [10000, 100000]!")
        else:
            return self.cleaned_data["amount"]


class LoadAdmin(admin.ModelAdmin):

    list_display = ("borrower", "amount", "period", "reason", "status", "applied_date")
    inlines = [RepaymentHistoryAdminForm]
    form = LoanAdminForm


admin.site.register(Loan, LoadAdmin)
