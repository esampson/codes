from django.db import models

# Create your models here.
class sphere(models.Model):
    app_id = models.AutoField(primary_key=True)
    longname = models.CharField(max_length=80, verbose_name='Merit Name')
    type = models.CharField(max_length=80, verbose_name='Merit Type')
    restricted = models.BooleanField(default=False)