from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app1.views.home', name='home')
]
