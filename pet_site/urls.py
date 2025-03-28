from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pet_site import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls", namespace="shop")),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
