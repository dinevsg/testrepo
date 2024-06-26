from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from cms.settings import DEBUG
from cms.web.views import HomeView

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home")
]

if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
