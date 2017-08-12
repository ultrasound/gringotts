from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.BankListView.as_view(), name="index"),
    url(r'^test/$', views.TestView.as_view())
]
