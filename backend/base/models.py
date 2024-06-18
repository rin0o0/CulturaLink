from djongo import models
from django.db import models as db_models
from django.utils.translation import gettext as _
# from djongo import models as djongo_models
from django.contrib.auth import get_user_model

from djongo.models.fields import ObjectIdField
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group


# Create your models here.
class CulturaUser(models.Model):
    user = models.CharField(max_length=255)
    fullname = models.CharField(max_length=120)
    country = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)


class Comment(models.Model):
    _id = ObjectIdField()
    post_id = models.CharField(
        max_length=255, null=True
    )
    replied_to = models.CharField(
        max_length=255,
    )
    author = models.CharField(max_length=255)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    


class Post(models.Model):
    _id = ObjectIdField()
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    content = models.TextField()
    country = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    


# class AppUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("An email is required.")
#         if not password:
#             raise ValueError("A password is required.")
#         if not username:
#             raise ValueError("A username is required.")
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, username, password=None):
#         if not email:
#             raise ValueError("An email is required.")
#         if not password:
#             raise ValueError("A password is required.")
#         if not username:
#             raise ValueError("A username is required.")
#         user = self.create_user(email, username, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user


# class AppUser(AbstractBaseUser, PermissionsMixin):
#     user_id = models.AutoField(primary_key=True)
#     email = models.EmailField(max_length=50)
#     username = models.CharField(max_length=50, unique=True)
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]
#     objects = AppUserManager()
#     groups = models.ManyToManyField(Group)
#     def __str__(self):
#         return self.username
