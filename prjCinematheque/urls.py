from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('core.urls') ),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

