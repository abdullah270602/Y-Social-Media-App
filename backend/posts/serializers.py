from rest_framework import serializers
from accounts.serializers import UserInfoSerializer
from posts.utlis import has_user_liked_post
from posts.models import Post, PostLike

class PostSerializers(serializers.ModelSerializer):
    created_by = UserInfoSerializer(read_only=True)
    time_since_creation = serializers.CharField(source='get_time_since_creation', read_only=True)
    liked = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at', 'time_since_creation', 'liked', 'like_count', )

    def get_liked(self, obj):
        current_user = self.context['user_id'] 
        return has_user_liked_post(current_user, obj.id)
    
    
    def get_like_count(self,obj):
        return PostLike.objects.filter(post=obj.id).count()
