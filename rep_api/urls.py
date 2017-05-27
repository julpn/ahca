from django.conf.urls import url
from rep_api.api import RepApi

from . import views

urlpatterns = [
    url(r'^$', RepApi.as_view(), name='index'),
]
