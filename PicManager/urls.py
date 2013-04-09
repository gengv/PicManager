from PicManager.view import hello, current_datetime, hours_ahead, var_test
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^hello/$', hello),
                       ('^time/$', current_datetime),
                       (r'^time/plus/(\d{1,2})/$', hours_ahead),
                       (r'^vt/(\d{1,2})/(\w+)/$', var_test),
                       
    # Examples:
    # url(r'^$', 'PicManager.views.home', name='home'),
    # url(r'^PicManager/', include('PicManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
