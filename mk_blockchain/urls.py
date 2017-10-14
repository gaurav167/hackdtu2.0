from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/$', views.index),
    url(r'^index/$', views.index),
    url(r'^home/index.html$', views.index),
    url(r'^login/$', views.login),
    url(r'^home/login.html$',views.login),
    url(r'^sell/$', views.sell),
    url(r'^buy/$', views.buy),
    url(r'^buys/$', views.buys),
    url(r'^sells/$', views.sells),
    url(r'^auth/$', views.auth),
]

