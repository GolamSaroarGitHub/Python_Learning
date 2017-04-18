from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list/', views.my_expenses,name='khoroch-list'),

]