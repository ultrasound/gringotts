from django import forms

from . import models


class BankForm(forms.ModelForm):
    class Meta:
        model = models.Bank
        fields = ["login", "password", "weboob_module"]
