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
        return f'{self.pk} | {self.name}'

    @property
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

    @property
    def block_users(self):
        """
        TwitterUsers self is blocking
        :return:
        """
        block_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_BLOCK
        )
        block_pk_list = block_relations.values_list('to_user', flat=True)
        block_users = TwitterUser.objects.filter(pk__in=block_pk_list)
        return block_users

    @property
    def followers(self):
        pk_list = self.relations_by_to_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING
        ).values_list('from_user', flat=True)
        return TwitterUser.objects.filter(pk__in=pk_list)

    def is_followee(self, to_user):
        """
        return boolean whether self is following to_user
        :param to_user:
        :return:
        """
        return self.following.filter(pk=to_user.pk).exists()

    def is_follower(self, to_user):
        """
        return boolean whether self is followed by to_user
        :param to_user:
        :return:
        """
        # if self in to_user.following:
        #     return True
        # else:
        #     return False
        return self.followers.filter(pk=to_user.pk).exists()

    def follow(self, to_user):
        """
        follow to_user (TwitterUser )
        :param to_user:
        :return:
        """
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_FOLLOWING,
        )

    def block(self, to_user):
        self.relations_by_from_user.filter(to_user=to_user).delete()
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_BLOCK,
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
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            # w/ params 'from_user', 'to_user'
            # block repeated saving w/ same params
            # ex) from_user = u1, to_user = u3,
            #       -> there could be only one relation b/w u1, u3
            ('from_user', 'to_user')
        )
