from django.contrib import admin
from loan.models import Loan, RepaymentHistory


class RepaymentHistoryAdminForm(admin.TabularInline):
    model = RepaymentHistory
    extra = 3

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class LoadAdmin(admin.ModelAdmin):

    list_display = ("borrower", "amount", "period", "reason", "status", "applied_date")
    inlines = [RepaymentHistoryAdminForm]

admin.site.register(Loan, LoadAdmin)
