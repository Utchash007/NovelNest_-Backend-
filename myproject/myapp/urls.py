from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import (NovelViewSet,NovelChapterViewSet,NovelInfoSet,
                    NovelUpdateViewSet,UserViewSet,BookmarkViewSet,
                    UserBookmarkViewSet,ReadHostoryViewSet,UserHistory,
                    AuthorViewSet, RatingViewSet)
=======
from .views import NovelViewSet,NovelChapterViewSet,NovelInfoSet,NovelUpdateViewSet,UserViewSet,BookmarkViewSet,UserBookmarkViewSet,ReadHostoryViewSet 
>>>>>>> parent of 36eee5f (Update)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register(r'novels', NovelViewSet)
router.register(r'users', UserViewSet)
router.register(r'chapter', NovelChapterViewSet)
router.register(r'novel-info', NovelInfoSet, basename='novel-info')
router.register(r'update_novel', NovelUpdateViewSet, basename='update_novel')
router.register(r'bookmark', BookmarkViewSet, basename='bookmark')
router.register(r'bookmarks', UserBookmarkViewSet, basename='bookmarks')
router.register(r'user_history', ReadHostoryViewSet,basename="user_history")
router.register(r'history', UserHistory, basename="history")
router.register(r'authors', AuthorViewSet, basename="authors")
router.register(r'rating', RatingViewSet, basename="rating")
urlpatterns = [
    path('api/', include(router.urls)),  #API routes prefixed with 'api/'
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]

