# extra fields on many-to-many relationships
import datetime

from django.db import models
from django.utils import timezone

__all__ = (
    'Post',
    'User',
    'PostLike',
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        # in MTM relationships, to be called by a different name from 'post_set'

        related_name='like_posts',
    )

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '"{title}" 글의 좋아요 ({name}, {date})'.format(
            title=self.post.title,
            name=self.user.name,
            date=datetime.strftime(
                timezone.localtime(self.created_date),
                '%Y.%m.%d'),
        )
