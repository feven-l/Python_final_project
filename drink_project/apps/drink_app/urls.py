from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main"),
    url(r'^infopage$', views.infopage),
    url(r'^suggest$', views.suggest, name="suggest"),

]
