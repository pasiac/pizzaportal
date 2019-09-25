from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("orders.urls", namespace="orders")),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include('django.contrib.auth.urls')),

]
