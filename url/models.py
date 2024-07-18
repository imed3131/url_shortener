from django.db import models

# Create your models here.
class Url_Map(models.Model):
    url = models.CharField(max_length=2000)
    url_shorten = models.CharField(max_length=200)