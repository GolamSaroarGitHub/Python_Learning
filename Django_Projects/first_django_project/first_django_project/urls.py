
from django.conf.urls import url
from django.contrib import admin

from first_django_project.first_django_app.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index,name='index'),

]
