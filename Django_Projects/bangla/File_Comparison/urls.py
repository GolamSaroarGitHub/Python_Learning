
from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^upload_file/$', views.model_form_upload, name='upload'),
    url(r'^comparison/$', views.show_difference, name='comparison'),

]
