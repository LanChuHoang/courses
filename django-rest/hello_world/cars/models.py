from django.db import models


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField(default=-1)
