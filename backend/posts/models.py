import uuid
from django.db import models
from django.utils.timezone import now
from accounts.models import User


class PostAttachments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="post_attachments")
    created_by = models.ForeignKey(
        User, related_name="post_attachments", on_delete=models.CASCADE
    )


class BasePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    attachments = models.ManyToManyField(PostAttachments, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="%(class)s_created_by", on_delete=models.CASCADE
    )

    def get_time_since_creation(self):
        delta = now() - self.created_at
        if delta.days >= 365:
            years = delta.days // 365
            return f"{years}year"
        elif delta.days >= 30:
            months = delta.days // 30
            return f"{months}months"
        elif delta.days >= 1:
            return f"{delta.days}days"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            return f"{hours}h"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            return f"{minutes}m"
        else:
            return "Just now"

    class Meta:
        abstract = True


class Post(BasePost):
    pass


class PostLike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    liked_by = models.ForeignKey(
        User, related_name="liked_posts", on_delete=models.CASCADE, db_index=True
    )
    post = models.ForeignKey(
        Post, related_name="post_likes", on_delete=models.CASCADE, db_index=True
    )
    liked_at = models.DateTimeField(auto_now_add=True)


class PostBookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bookmarked_by = models.ForeignKey(User, related_name='bookmarked_posts', on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey(Post, related_name='post_bookmarks', on_delete=models.CASCADE, db_index=True)
    bookmarked_at = models.DateTimeField(auto_now_add=True)