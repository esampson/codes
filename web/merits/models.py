from django.db import models

# Create your models here.
class merit(models.Model):
    app_id = models.AutoField(primary_key=True)
    longname = models.CharField(max_length=80, verbose_name='Merit Name')
    type = models.CharField(max_length=80, verbose_name='Merit Type')
    range = models.TextField(verbose_name='Background')
    restrictedNotes = models.CharField(max_length=80, verbose_name='Valid notes')
    prereq = models.CharField(max_length=80, verbose_name='Prerequisites')
    restricted = models.BooleanField(default=False)