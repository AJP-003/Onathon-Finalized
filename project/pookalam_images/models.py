from email.mime import image
from django.db import models

# Create your models here.

class Pookal(models.Model):
    image = models.URLField()
    red = models.IntegerField()
    yellow = models.IntegerField()
    white = models.IntegerField()
    orange = models.IntegerField()
    violet = models.IntegerField()
    green = models.IntegerField()
    pink = models.IntegerField()

    def __str__(self):
         return self.image
    #created to store each value for the 