from .models import PostLike



def has_user_liked_post(user,post):
    return PostLike.objects.filter(liked_by=user, post=post).exists()