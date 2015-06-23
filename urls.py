from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
#from app1.views import home1

urlpatterns = [
    
    url(r'^$', 'app1.views.spot_list', name='spot_list'),
    url(r'^spot/(?P<pk>[0-9]+)/$', 'app1.views.spot_detail'),
    url(r'^spot/new/$', 'app1.views.spot_new', name='spot_new'),
    #url(r'', include('app1.urls'))
    #url(r'^$admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^app1/', include('app1.urls')),
    #url(r'^$', home1.as_view(), name='home1'),
    url(r'^admin/', include(admin.site.urls)),
]
