from django.db import models

# Create your models here.


class Bank(models.Model):
    username = models.CharField()
    password = models.CharField()
    name = models.CharField()


class Account(models.Model):
    name = models.CharField()
    balance = models.FloatField()
    bank = models.ForeignKey('Bank')


class Entry(models.Model):
    title = models.CharField()
    amount = models.FloatField()
    currency = models.CharField()
    account = models.ForeignKey('Account')


class Category(models.Model):
    name = models.CharField()
    color = models.CharField()
