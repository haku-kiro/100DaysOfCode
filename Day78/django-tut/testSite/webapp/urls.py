from django.conf.urls import url
from . import views # The period is just the current package

urlpatterns = [
    url(r'^$', views.index, name='index') # the regex is the start and the end, meaning an index (nothing attached)
]