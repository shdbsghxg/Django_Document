from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    """
    MTM model w/ self
    """
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    def __str__(self):
        # person1 [friends : friend1, friend2]

        # for loop
        friends_string = ''
        for friend in self.friends.all():
            friends_string += friend.name
            friends_string += ','
        friends_string = friends_string[:-2]

        # list comprehension
        friends_string = ', '.join([friend.name for friend in self.friends.all()])

        # Manager-value_list
        # get value of 'name' field in DB
        friends_string = ', '.join(self.friends.values_list('name', flat=True))

        return '{name} (friend: {friends})'.format(
            name=self.name,
            friends=friends_string,
        )
