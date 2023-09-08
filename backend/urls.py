from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from offers.views import index
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("api/", include(("api.urls", "api"), namespace="api")),
    path("api-token-auth", views.obtain_auth_token),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "My Daily Basket Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to MDB admin site"
