from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/', include('accounts.urls', namespace = 'accounts')),
	path('admin/', admin.site.urls),
    path('', include('room.urls',namespace = 'room')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)