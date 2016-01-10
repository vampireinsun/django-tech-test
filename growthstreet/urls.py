from django.conf.urls import include, url
from growthstreet import views
from django.contrib import admin

urlpatterns = [
    url(r'^index/$', views.index_page),
    url(r'^borrower', include('borrower.urls')),
    url(r'^loans/', include('loan.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
