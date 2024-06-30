from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_username(sender, instance, created, **kwargs):
    if created:
        instance.username = instance.generate_random_username()
        instance.save()
