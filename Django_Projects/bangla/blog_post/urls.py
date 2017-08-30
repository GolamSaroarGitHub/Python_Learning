
from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^post_lists/$', views.post_list,name='post_lists'),
    url(r'^single_post/(?P<post_id>[0-9]+)/$', views.single_post,name='single_post'),
    url(r'^add_post/$', views.add_posts, name='add_post'),

]
