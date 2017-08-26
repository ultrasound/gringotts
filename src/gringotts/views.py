from django.views import generic
from django.urls import reverse_lazy

from . import models, forms


class BankListView(generic.ListView):
    model = models.Bank
    template_name = "bank/list.html"
    context_object_name = "banks"


class BankCreateView(generic.edit.CreateView):
    model = models.Bank
    form_class = forms.BankForm
    template_name = "bank/form.html"
    success_url = reverse_lazy("gringotts:index")


class BankUpdateView(generic.edit.UpdateView):
    model = models.Bank
    template_name = "bank/form.html"
    form_class = forms.BankForm
    success_url = reverse_lazy("gringotts:index")


class BankDeleteView(generic.edit.DeleteView):
    model = models.Bank
    success_url = reverse_lazy("gringotts:index")
    template_name = "bank/confirm_delete.html"
