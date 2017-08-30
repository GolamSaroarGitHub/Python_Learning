
from django.conf.urls import url,include
from django.contrib import admin
from File_Comparison import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog_post.urls')),
    url(r'^cost/', include('cost_management.urls')),
    url(r'^home/', include('File_Comparison.urls')),

]
