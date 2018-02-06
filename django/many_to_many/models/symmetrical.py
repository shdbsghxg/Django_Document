from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
    )

    class Meta:
        verbose_name_plural = 'Symmetrical - InstagramUsers'

    def __str__(self):
        return self.name



