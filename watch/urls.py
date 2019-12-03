
from django.contrib import admin
from django.conf.urls import url, include

from django.contrib.auth import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('neighborhood.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {'next_page':'/'}),
   
]
