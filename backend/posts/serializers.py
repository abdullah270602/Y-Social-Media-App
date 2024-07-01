from rest_framework import serializers
from accounts.serializers import UserInfoSerializer
from posts.models import Post


class PostSerializers(serializers.ModelSerializer):
    created_by = UserInfoSerializer(read_only=True)
    time_since_creation = serializers.CharField(source='get_time_since_creation', read_only=True)
    

    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at', 'time_since_creation',)
