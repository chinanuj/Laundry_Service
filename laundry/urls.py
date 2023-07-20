from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("laundry_app.urls")),
    path('clothselection/', include("clothselection.urls")),
    path('account/',include("account.urls")),
    path('clothselection2/',include("clothselection2.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)