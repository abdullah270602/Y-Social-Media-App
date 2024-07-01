from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.serializers import PostSerializers
from posts.forms import PostForm


@api_view(["POST"])
def create_post(request):
    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        serializer = PostSerializers(post, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET'])
def get_posts(request):
    try:
        posts = Post.objects.all().order_by('-created_at')
        
        serializer = PostSerializers(posts, many=True, context={'request': request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)