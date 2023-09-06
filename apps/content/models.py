from django.db import models

from shared.models import BaseModel, CustomFileExtensionValidator, unique_id

file_ext_validator = CustomFileExtensionValidator(('mp4', 'mkv', 'avi', 'webm', '3gp', 'jpg', 'jpeg', 'png', 'webp'))


class Post(BaseModel):
    id = models.CharField(primary_key=True, default=unique_id, max_length=255)
    caption = models.TextField(null=True, blank=True)
    author = models.ForeignKey('users.UserModel', on_delete=models.CASCADE)
    media = models.ManyToManyField('content.Media', related_name='medias')
    location = models.CharField(max_length=255, null=True, blank=True)
    likes = models.ManyToManyField('content.Like', related_name='posts')
    comments = models.ManyToManyField('content.CommentPost', related_name='posts')

    def __str__(self):
        return self.caption

    @property
    def get_number_of_likes(self):
        return self.likes.count()

    @property
    def get_number_of_comments(self):
        return self.comments.count()


class Reel(BaseModel):
    id = models.CharField(primary_key=True, default=unique_id, max_length=36)
    caption = models.TextField(null=True, blank=True)
    author = models.ForeignKey('users.UserModel', on_delete=models.CASCADE)
    media = models.FileField(upload_to='reels/', validators=[CustomFileExtensionValidator(['mp4', 'avi', 'mkv'])])
    location = models.CharField(max_length=255, null=True, blank=True)
    likes = models.ManyToManyField('content.Like', related_name='reels')
    comments = models.ManyToManyField('content.CommentReel', related_name='reels')

    @property
    def get_number_of_likes(self):
        return self.likes.count()

    @property
    def get_number_of_comments(self):
        return self.comments.count()


class Media(models.Model):
    file = models.FileField(upload_to='posts/', validators=(file_ext_validator, ))


class CommentReel(models.Model):
    user = models.ForeignKey('users.UserModel', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True)
    reel = models.ForeignKey('content.Reel', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class CommentPost(CommentReel):
    reel = None
    post = models.ForeignKey('content.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Like(models.Model):
    user = models.ForeignKey('users.UserModel', on_delete=models.CASCADE)

    def __str__(self):
        return 'Like: ' + self.user.username




