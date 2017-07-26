from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Shop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Rating(models.Model):
    shop = models.ForeignKey(Shop)
    score = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])

