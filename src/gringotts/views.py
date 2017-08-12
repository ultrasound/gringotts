from django.views import generic

from . import models


class BankListView(generic.ListView):
    model = models.Bank
    template_name = "banks_list.html"
