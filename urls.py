from django.conf.urls.defaults import *
from core.views import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
	(r'^$', 'direct_to_template', {'template': 'index.html'}),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),
    # Example:
    # (r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'edia/(?P<path>.*)$',
        'django.views.static.serve', 
        {'document_root':settings.MEDIA_ROOT}),
    )

