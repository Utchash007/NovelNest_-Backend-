from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NovelViewSet,UserViewSet,NovelChapterViewSet,NovelInfoSet,NovelUpdateViewSet
router = DefaultRouter()
router.register(r'novels', NovelViewSet)
router.register(r'users', UserViewSet)
router.register(r'chapter', NovelChapterViewSet)
router.register(r'novel-info', NovelInfoSet, basename='novel-info')
router.register(r'update_novel', NovelUpdateViewSet, basename='update_novel')
urlpatterns = [
    path('api/', include(router.urls)),  #API routes prefixed with 'api/'
    
]

