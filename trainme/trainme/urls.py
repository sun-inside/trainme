from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api.resources import EventResource, CoachResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CoachResource())
v1_api.register(EventResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
