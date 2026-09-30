from django.db import models

# Create your models here.

class TurfRegister(models.Model):

    team_name = models.CharField(max_length=200)

    phone_number = models.PositiveIntegerField()

    date = models.DateTimeField()

    duration = models.CharField(max_length=150)

    def __str__(self):

        self.team_name