from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (NovelViewSet,NovelChapterViewSet,NovelInfoSet,
                    NovelUpdateViewSet,AuthorViewSet)
router = DefaultRouter()
router.register(r'novels', NovelViewSet)
router.register(r'chapter', NovelChapterViewSet)
router.register(r'novel-info', NovelInfoSet, basename='novel-info')
router.register(r'update_novel', NovelUpdateViewSet, basename='update_novel')
router.register(r'authors', AuthorViewSet, basename="authors")

urlpatterns =[
    path('api/', include(router.urls))
]