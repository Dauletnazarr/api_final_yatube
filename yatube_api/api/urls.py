from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
)


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/comments/', CommentViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='post-comments'),

    path('v1/posts/<int:post_id>/comments/<int:pk>/', CommentViewSet.as_view(
        {'get': 'retrieve', 'put': 'update',
         'patch': 'partial_update', 'delete': 'destroy'}),
         name='post-comment-detail'),

]
