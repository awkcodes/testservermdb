from django.urls import path, include

urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]
