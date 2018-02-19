from django.db import models
from django.db.models import Manager


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# custom manager
class NewManager(Manager):
    def get_queryset(self):
        print('NewManager get_queryset')
        return super().get_queryset()


# holding custom manager as self's attr directly
class MyPerson1(Person):
    secondary = NewManager()

    class Meta:
        proxy = True


# ABC model holding custom manager as self' attr
class ExtraManagerModel(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True


# inheriting ABC model
# holding secondary indirectly
class MyPerson2(Person, ExtraManagerModel):
    class Meta:
        proxy = True
