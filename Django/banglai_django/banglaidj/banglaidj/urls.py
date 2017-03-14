
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('blog_post.urls')),
    url(r'^cost/', include('cost_management.urls'),name='cost'),

]
