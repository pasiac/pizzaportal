from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("orders.urls")),
    path("menu", include("orders.urls")),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include('django.contrib.auth.urls')),

]
