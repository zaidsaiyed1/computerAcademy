from django.db import models

# Create your models here.
class Supadmin(models.Model):
    aid = models.PositiveIntegerField()
    aname = models.CharField(max_length=20)
    apass = models.IntegerField()

class Meta:
    db_table = "Supadmin"

class user_details(models.Model):
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    cp = models.CharField(max_length=10)
    diabi = models.CharField(max_length=10)
    sob = models.CharField(max_length=10)
    bps = models.CharField(max_length=10)
    fati = models.CharField(max_length=10)
    nov = models.CharField(max_length=10)
    ioh = models.CharField(max_length=10)
    es = models.CharField(max_length=10)
    hhd = models.CharField(max_length=10)


class Meta:
    db_table = "user_details"