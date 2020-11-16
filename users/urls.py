from django.conf.urls import include, url
from users.views import dashboard, register
from . import views

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^bank_accounts/", views.bank_accounts, name="bank_accounts"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
]
