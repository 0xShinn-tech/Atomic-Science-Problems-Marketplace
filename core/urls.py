from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProblemViewSet,
    SolutionViewSet,
    CommentViewSet,
    ProfileViewSet
)

router = DefaultRouter()
router.register(r'problems', ProblemViewSet)
router.register(r'solutions', SolutionViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]