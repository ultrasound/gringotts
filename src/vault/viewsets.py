from djangorestframework import viewsets
from weboob.core import Weboob
from weboob.capabilities.bank import CapBank

from vault import serializers


class AccountViewSet(viewsets.Viewset):
    serializer_class = serializers.AccountSerializer

    def get(self):
        w = Weboob()
        w.load_backends(CapBank)
        accounts = list(w.iter_accounts())
        return self.serializer_class(data=accounts)


