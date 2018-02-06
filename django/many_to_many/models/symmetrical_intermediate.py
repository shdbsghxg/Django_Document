from django.db import models


class TwitterUser(models.Model):
    """
    self follows A
        self is follower of A
        A is followee of self
    A and self follow each other
        A and self are friends

    w/ block
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',
    )


class Relation(models.Model):
    """
    relation b/w users
    not only MTM of itself, but also intermediate
    additional receiving info is a type of relations
    """
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
