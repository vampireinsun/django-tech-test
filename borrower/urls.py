from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'register/', views.register),
    url(r'login/', views.login_view),
    url(r'password_change/', auth_views.password_change),
    url(r'password_reset/', auth_views.password_reset),
    url(r'logout/', views.logout_view),
    url(r'profile/', views.borrower_profile_view),
    url(r'(?P<borrower_business_id>\d+)/business/update/', views.borrower_update_business_view),
    url(r'(?P<borrower_business_id>\d+)/business/', views.borrower_business_view),
]
