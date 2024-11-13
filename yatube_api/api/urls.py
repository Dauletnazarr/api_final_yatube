from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import (
    PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
)


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('comments', CommentViewSet, basename='post-comments')
urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    path('v1/', include(posts_router.urls)),
]
