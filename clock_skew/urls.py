from django.conf.urls import patterns, url
from clock_skew import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='clock_skew_index'),
    url(r'^time_stamp/$', views.time_stamp, name='clock_skew_time_stamp'),
)
