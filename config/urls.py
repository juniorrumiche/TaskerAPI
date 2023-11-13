from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/api/schema/swagger/"), name="index"),
    path("api/", include("api.urls")),
]
