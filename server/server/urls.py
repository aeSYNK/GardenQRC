from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from menuapi.views import *

router = SimpleRouter()
router.register(r'room', RoomViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
