from django.db import models


class Manufacturer(models.Model):
    name = models.CharField('brand', max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        verbose_name='maker'
    )
    name = models.CharField(max_length=60)

    def __str__(self):
        return '{} {}'.format(
            self.manufacturer,
            self.name,
        )