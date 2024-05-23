from django.contrib import admin
from django.urls import include, path

from app.settings import DEBUG

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("catalog/", include("goods.urls")),
]

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]