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
        r'^banks/(?P<pk>[0-9]+)/edit$',
        views.BankCreateView.as_view(),
        name="bank-edit"
    ),
    url(
        r'^banks/(?P<pk>[0-9]+)/delete$',
        views.BankDeleteView.as_view(),
        name="bank-delete"
    ),

]
