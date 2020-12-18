from django.db import models
from django.contrib.auth.models import User

from datetime import date

# Create models that store the required information in the database.


class Food(models.Model):
    name = models.CharField(max_length=200, null=False)
    quantity = models.PositiveIntegerField(null=False, default=0)
    date = models.DateField()
    person_of = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PostFood(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    calorie_amount = models.FloatField(default=0, null=True, blank=True)
    amount = models.FloatField(default=0)
