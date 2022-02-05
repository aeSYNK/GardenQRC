from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from menuapi.views import *

router = SimpleRouter()
# router.register(r'room', RoomViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth-token', include('djoser.urls.authtoken')),
    re_path(r'^register/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
