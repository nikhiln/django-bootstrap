from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
from bttest import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bttest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^','bttest.views.index'),
    url(r'^delete/(?P<memberid>\w+)/$','bttest.views.delete'),
    #url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        )
    urlpatterns += patterns('',
                 (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
            )
