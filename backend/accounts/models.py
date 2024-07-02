import random
import string
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
import uuid

class CustomUserManager(UserManager):

    def _create_user(self, username, email, password, first_name=None, last_name=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, first_name=None, last_name=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, first_name="None", last_name="None", **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        return self._create_user(username, email, password, first_name, last_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True,)
    full_name = models.CharField(max_length=30, blank=False, null=False,)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False) 
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True, null=True)
    profile_bio = models.TextField(blank=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [""]

    # CustomUserManager for custom user operations and queries.
    objects = CustomUserManager()

    def __str__(self):
        return self.full_name
    
    def generate_random_username(self):
        name_part = ''.join(e for e in self.full_name if e.isalnum())
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        return f"{name_part}_{random_suffix}"
    
    class Meta:
        ordering = ["-date_joined"]
        verbose_name = "user"
        verbose_name_plural = "users"


class EmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verification')
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    token_expiration = models.DateTimeField(blank=False,null=False)


    def is_token_expired(self):
        return self.token_expiration < timezone.now()


    @staticmethod
    def generate_token():
        return uuid.uuid4()
    
    
class Followers(models.Model):
    """
    Represents the relationship between users where one user is followed by another user.
   
        followed_user (ForeignKey to User): The user who is being followed by others.
        follower (ForeignKey to User): The user who is following other users.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    followed_user = models.ForeignKey(User, related_name='follower_relationships', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='following_relationships', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    