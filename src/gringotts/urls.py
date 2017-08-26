from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.BankListView.as_view(), name="index"),
    url(
        r'^banks/create/$',
        views.BankCreateView.as_view(),
        name="bank-create"
    ),
    url(
        r'^banks/(?P<pk>[0-9]+)/update$',
        views.BankUpdateView.as_view(),
        name="bank-update"
    ),
    url(
        r'^banks/(?P<pk>[0-9]+)/delete$',
        views.BankDeleteView.as_view(),
        name="bank-delete"
    ),
]
