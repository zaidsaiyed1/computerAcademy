from django.db import models

# Create your models here.
class Supadmin(models.Model):
    aid = models.PositiveIntegerField()
    aname = models.CharField(max_length=20)
    apass = models.IntegerField()

class Meta:
    db_table = "Supadmin"

class user_details(models.Model):
    city = models.CharField(max_length=10, default='NUll')
    state = models.CharField(max_length=10,default='NUll')
    country = models.CharField(max_length=10,default='NUll')
    age = models.IntegerField()
    sex = models.CharField(max_length=10,default='NUll')
    cp = models.CharField(max_length=10, default='Null')
    diabi = models.CharField(max_length=10, default='Null')
    sob = models.CharField(max_length=10, default='Null')
    bps = models.CharField(max_length=10, default='Null')
    fati = models.CharField(max_length=10, default='Null')
    nov = models.CharField(max_length=10, default='Null')
    ioh = models.CharField(max_length=10, default='Null')
    es = models.CharField(max_length=10, default='Null')
    hhd = models.CharField(max_length=10, default='Null')


class Meta:
    db_table = "user_details"

class user_data1(models.Model):
    uname = models.CharField(max_length=30, default='NUll')
    ucountry = models.CharField(max_length=20, default='NUll')
    uage = models.IntegerField()
    usex = models.CharField(max_length=10, default='NUll')
    uemail = models.EmailField(max_length=60, default='NUll')
    ufeedb = models.CharField(max_length=200, default='NUll')

class Meta:
    db_table = "user_data1"