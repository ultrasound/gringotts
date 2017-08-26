from django.urls import reverse_lazy
import pytest

from gringotts import models


@pytest.mark.django_db
def test_bank_create(client):
    url = reverse_lazy("gringotts:bank-create")
    bank_vars = {
        "login": "Test",
        "password": "1234",
        "weboob_module": "bp"
    }

    response = client.post(
        url, bank_vars
    )
    assert 302 == response.status_code
    assert models.Bank.objects.count() == 1
    bank = models.Bank.objects.first()
    assert bank.login == bank_vars["login"]
    assert bank.password == bank_vars["password"]
    assert bank.weboob_module == bank_vars["weboob_module"]
    assert response.url == reverse_lazy("gringotts:index")


@pytest.mark.django_db
def test_bank_update(client):
    bank = models.Bank.objects.create(
        login="Test", password="1234", weboob_module="bp"
    )
    url = reverse_lazy("gringotts:bank-update", kwargs={"pk": bank.pk})

    response = client.get(url)
    assert response.status_code == 200
    bank_response = response.context["object"]
    assert bank_response.login == bank.login
    assert bank_response.password == bank.password
    assert bank_response.weboob_module == bank.weboob_module

    response = client.post(
        url,
        {
            "login": bank.login,
            "password": bank.password + "z",
            "weboob_module": bank.weboob_module
        }
    )

    assert models.Bank.objects.first().password == bank.password + "z"


@pytest.mark.django_db
def test_bank_delete(client):
    bank = models.Bank.objects.create(
        login="Test", password="1234", weboob_module="bp"
    )
    number_of_banks = models.Bank.objects.count()
    url = reverse_lazy("gringotts:bank-delete", kwargs={"pk": bank.pk})

    response = client.delete(url)
    assert response.status_code == 302
    assert models.Bank.objects.count() == number_of_banks - 1
