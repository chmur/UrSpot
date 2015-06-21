from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app1.views.home', name='home'),
    url(r'^$admin/doc/', include('django.contrib.admindocs.urls')),
]
