from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet, SentenciadoViewSet, PavilhaoViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('sentenciados', SentenciadoViewSet)
router.register('pavilhoes', PavilhaoViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/admin/
    path('admin/', admin.site.urls),
]
