
from django.conf.urls import url
from django.contrib import admin

from banglai_django.first_django_project.first_project.first_app.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),-
    url(r'^$', index,name='index'),

]
