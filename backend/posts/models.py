import uuid
from django.db import models
from django.utils.timesince import timesince
from accounts.models import User

class PostAttachments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)


class BasePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    attachments = models.ManyToManyField(PostAttachments, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by', on_delete=models.CASCADE)
    
    def get_time_since_creation(self):
        return timesince(self.created_at)
    
    class Meta:
        abstract = True
        

class Post(BasePost):
    pass
