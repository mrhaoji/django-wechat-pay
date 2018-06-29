from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from pay import views

urlpatterns = [
    url(r'^wxpay/', views.wxpay),
    url(r'^wxpayNotify/', views.wxpayNotify),
]
