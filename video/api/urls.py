from django.urls import path, include
from rest_framework import routers
from video.api.views import VideoViewSet


router = routers.DefaultRouter()
router.register(r'video-upload', VideoViewSet, basename='video-upload')

app_name = 'video'

urlpatterns = [
    path('', include(router.urls))
]
