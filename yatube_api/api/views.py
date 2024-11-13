from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, serializers, filters, mixins
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)
from api.permissions import IsAuthorOrReadOnly
from posts.models import Post, Group, Comment, Follow

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления постами.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """
        Устанавливаем текущего пользователя как автора поста при создании.
        """
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet только для чтения групп.
    Создание группы через API запрещено.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """
    ViewSet для управления подписками.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """
        Возвращаем только подписки текущего пользователя.
        """
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Проверяем подписку и предотвращаем самоподписку или дублирование.
        """
        following = serializer.validated_data['following']
        if self.request.user == following:
            raise serializers.ValidationError(
                'Вы не можете подписаться на самого себя!')

        if Follow.objects.filter(
            user=self.request.user,
            following=following,
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя!')

        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления комментариями.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Возвращаем комментарии, привязанные к конкретному посту.
        """
        post = get_object_or_404(Post, id=self.kwargs['post_pk'])
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        """
        Создаём комментарий, привязанный к посту.
        """
        post = get_object_or_404(Post, id=self.kwargs['post_pk'])
        serializer.save(post=post, author=self.request.user)
