from django.urls import path, include
from rest_framework.routers import DefaultRouter


from myvideo.api import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'myvideo'

urlpatterns = [
    path('', include(router.urls))
]
