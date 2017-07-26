from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Shop(models.Model):
    name = models.CharField(max_length=100)
    score = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def score_point(self):
        return self.score / 10

    def calc_score(self):
        avg = self.rating_set.all().aggregate(Avg('score'))['score__avg']
        self.score = int(avg * 10)
        self.save()


class Rating(models.Model):
    shop = models.ForeignKey(Shop)
    score = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])

