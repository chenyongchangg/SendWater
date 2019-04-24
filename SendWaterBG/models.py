from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    passwd = models.CharField(max_length=130)


class OfferMan(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=230)
    number = models.CharField(max_length=30)
    othermsg = models.CharField(max_length=130)


class CommitTable(models.Model):
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)
    time = models.CharField(max_length=230)
    address = models.CharField(max_length=130)
    userPhone = models.CharField(max_length=130)
    otherMsg = models.CharField(max_length=230)
    kind = models.CharField(max_length=130, default="none")


class admin(models.Model):
    name = models.CharField(max_length=30)
    passed = models.CharField(max_length=130)
    boss = models.CharField(max_length=130)

