from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views  import *

router = DefaultRouter()

router.register(r'bookmarks', UserBookmarkViewSet, basename='bookmarks')
router.register(r'user_history', ReadHostoryViewSet,basename="user_history")
router.register(r'history', UserHistory, basename="history")
urlpatterns = [
    path('api/',include(router.urls)),
]