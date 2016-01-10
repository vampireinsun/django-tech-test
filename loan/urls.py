from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'(?P<borrower_loan_id>\d+)/loan/update/', views.update_loan_view),
    url(r'(?P<borrower_loan_id>\d+)/loan/', views.loan_view),
]
