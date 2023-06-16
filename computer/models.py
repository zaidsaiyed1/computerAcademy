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
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exng = models.IntegerField()
    oldpeak = models.IntegerField()
    slp = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
    num = models.IntegerField()


class Meta:
    db_table = "user_details"