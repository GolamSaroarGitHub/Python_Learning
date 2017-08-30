
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^list/$',views.costs,name='cost-list'),
    url(r'^add/$', views.add_Expenses, name='add-cost'),

]
