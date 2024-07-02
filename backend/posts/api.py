from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from accounts.serializers import UserInfoSerializer
from posts.utlis import has_user_bookmarked_post, has_user_liked_post
from posts.models import Post, PostBookmark, PostLike
from posts.serializers import PostSerializers
from posts.forms import PostForm


@api_view(["POST"])
def create_post(request):
    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        serializer = PostSerializers(post, context={'user_id': request.user.id})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET'])
def get_posts(request):
    try:
        posts = Post.objects.all().order_by('-created_at')
        
        serializer = PostSerializers(posts, many=True, context={'user_id': request.user.id})
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['POST'])
def toggle_post_like(request, postId):
    user = request.user
    post = get_object_or_404(Post, id=postId)

    try:
        if has_user_liked_post(user, post):
            post_like = PostLike.objects.get(liked_by=user, post=post)
            post_like.delete()
            return Response({'context': 'unliked'}, status=status.HTTP_200_OK)
        else:
            post_like = PostLike(liked_by=user, post=post)
            post_like.save()
            return Response({'context': 'liked'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['POST'])
def toggle_post_bookmark(request, postId):
    user = request.user
    post = get_object_or_404(Post, id=postId)

    try:
        if has_user_bookmarked_post(user, post):
            post_bookmark = PostBookmark.objects.get(bookmarked_by=user, post=post)
            post_bookmark.delete()
            return Response({'context': 'unbookmarked'}, status=status.HTTP_200_OK)
        else:
            post_bookmark = PostBookmark(bookmarked_by=user, post=post)
            post_bookmark.save()
            return Response({'context': 'bookmarked'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def get_users_post_list(request, username):
    try:
        user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(created_by=user).order_by('-created_at')

        post_serializer = PostSerializers(posts, many=True, context={'user_id': request.user.id})
        user_serializer = UserInfoSerializer(user)
        
        return Response({'posts': post_serializer.data, 'user': user_serializer.data}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)