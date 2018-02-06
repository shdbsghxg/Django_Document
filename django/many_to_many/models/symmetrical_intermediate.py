from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


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

    def __str__(self):
        return self.name

    def following(self):
        """
        TwitterUser list followed by self
        :return:
        """
        # query set w/ from_user=self, type=following
        following_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        # pk list of the upper query set
        following_pk_list = following_relations.values_list('to_user', flat=True)
        # if TwitterUser's pk is in pk list(the upper),
        # add to following_users var
        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)
        return following_users


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
        # when self as from_user, to get relations
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # when self as to_user, to get relations
        related_name='relations_by_to_user',
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
