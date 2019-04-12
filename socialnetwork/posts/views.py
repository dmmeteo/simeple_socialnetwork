from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import LikePostSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API View set that perform a CRUD with a posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['put'],
            detail=True,
            permission_classes=[IsAuthenticated],
            serializer_class=LikePostSerializer)
    def likes(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        user = str(request.user.pk)
        # Set increment and decrement instances
        inc, dec = post.like, post.unlike
        if not request.data['like']:
            inc, dec = dec, inc
        inc.set(user)
        dec.remove(user)
        post.save()

        serializer = PostSerializer(post, context={'request': request})
        return JsonResponse(serializer.data)
