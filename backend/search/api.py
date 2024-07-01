
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
from posts.models import Post
from accounts.serializers import UserInfoSerializer
from posts.serializers import PostSerializers
from rest_framework import status  # type: ignore


@api_view(['POST'])
def search(request):
    try:
        data = request.data
        query = data.get('query', '')

        # Search users
        users = User.objects.filter(username__icontains=query)
        user_serializer = UserInfoSerializer(users, many=True)

        # Search posts
        posts = Post.objects.filter(Q(body__icontains=query) | Q(created_by__username__icontains=query))
        post_serializer = PostSerializers(posts, many=True, context={'user_id': request.user.id})

        return Response({
            'user_results': user_serializer.data,
            'post_results': post_serializer.data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
