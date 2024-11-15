from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='post-comments'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
