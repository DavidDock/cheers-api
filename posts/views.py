from django.db.models import Count
from rest_framework import generics, permissions, filters
from cheers_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        stars_count=Count('stars', distinct=True),
        cheers_count=Count('cheers', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'type',
    ]
    ordering_fields = [
        'stars_count',
        'cheers_count',
        'comments_count',
        'stars__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        stars_count=Count('stars', distinct=True),
        cheers_count=Count('cheers', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
