from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RatingViewSet

router=DefaultRouter()
router.register(r'rating', RatingViewSet, basename="rating")
urlpatterns=[
    path('api/', include(router.urls))
]