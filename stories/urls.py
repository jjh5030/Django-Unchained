from django.conf.urls import patterns, include, url
from stories import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^story/$', views.story, name='story'),
)
