from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clock_skew/', include('clock_skew.urls')),
    url(r'^$', RedirectView.as_view(url='/clock_skew/')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
  )
)
