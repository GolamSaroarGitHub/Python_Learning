from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home,name='index' ),
    url(r'^show_all_posts/', views.show_all_posts,name='show_all_posts'),
    url(r'^single_post/(?P<post_id>[0-9]+)/', views.single_post,name='single_post'),

]
