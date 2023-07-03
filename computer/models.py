from django.db import models

# Create your models here.
class Supadmin(models.Model):
    aid = models.PositiveIntegerField()
    aname = models.CharField(max_length=20)
    apass = models.IntegerField()

class Meta:
    db_table = "Supadmin"

class user_details(models.Model):
    age = models.PositiveIntegerField()
    sex = models.PositiveIntegerField()
    cp = models.IntegerField()
    diabi = models.IntegerField()
    sob = models.IntegerField()
    bps = models.IntegerField()
    fati = models.IntegerField()
    hr = models.IntegerField()
    nov = models.IntegerField()
    ioh = models.IntegerField()
    es = models.IntegerField()



class Meta:
    db_table = "user_details"