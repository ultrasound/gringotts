from django.db import models
from enum import Enum
from weboob.core import Weboob
from weboob.capabilities.bank import CapBank


class Currencies(Enum):
    POUND = "GBP"
    EURO = "EUR"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Bank(models.Model):
    @staticmethod
    def banks_supported():
        """
        Return all the banks supported by weboob.
        :return: [(module_name, Module_description)]
        """
        banks_supported = []
        weboob = Weboob()
        modules = weboob.repositories.get_all_modules_info(CapBank)
        for bank_module_name, info in modules.items():
            banks_supported.append((bank_module_name, info.description))

        return banks_supported

    login = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    weboob_module = models.CharField(
        max_length=32,
        choices=banks_supported.__func__(),
        blank=False
    )

    @property
    def name(self):
        return self.get_weboob_module_display()


class Account(models.Model):
    name = models.CharField(max_length=32)
    balance = models.FloatField()
    bank = models.ForeignKey('Bank')
    currency = models.CharField(max_length=3, choices=Currencies.choices())


class Entry(models.Model):
    title = models.CharField(max_length=128)
    amount = models.FloatField()
    account = models.ForeignKey('Account')
    category = models.ForeignKey('Category')


class Category(models.Model):
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=6)
