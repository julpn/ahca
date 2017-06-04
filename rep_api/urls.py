from django.conf.urls import url
from rep_api.api import RepApi, RandomRepApi

from . import views

urlpatterns = [
    url(r'^$', RepApi.as_view(), name='index'),
    url(r'^random/', RandomRepApi.as_view(), name='random'),
]
