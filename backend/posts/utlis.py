from .models import PostBookmark, PostLike



def has_user_liked_post(user,post):
    return PostLike.objects.filter(liked_by=user, post=post).exists()

def has_user_bookmarked_post(user,post):
    return PostBookmark.objects.filter(bookmarked_by=user, post=post).exists()