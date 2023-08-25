from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserModel(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='users/', blank=True, default='https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg', null=True)
    followers = models.ManyToManyField('UserModel', related_name='followers_profile', symmetrical=False, blank=True)
    following = models.ManyToManyField('UserModel', related_name='following_profile', symmetrical=False, blank=True)
    bio = models.TextField(blank=True, null=True)

    @property
    def following_count(self):
        return self.following.count()

    @property
    def followers_count(self):
        return self.followers.count()

    def __str__(self):
        return self.username



