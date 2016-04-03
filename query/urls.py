# encoding: utf-8


from django.conf.urls import patterns, url

urlpatterns = patterns('query.views',
    url(r'^$', 'index', name='index'),
    url(r'^detail/(?P<bid>\d+)/$', 'detail', name='detail'),
    url(r'^add_business/$', 'add_business', name='add_business'),
    url(r'^add_customer/$', 'add_customer', name='add_customer'),
)
