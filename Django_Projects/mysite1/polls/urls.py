from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/result/$', views.result, name='result'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

]

