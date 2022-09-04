from email.mime import image
from django.db import models

# Create your models here.

class Tables(models.Model):
    image = models.ImageField()
    red = models.IntegerField()
    yellow = models.IntegerField()
    white = models.IntegerField()
    orange = models.IntegerField()
    violet = models.IntegerField()
    green = models.IntegerField()
    pink = models.IntegerField()
    #created to store each value for the 