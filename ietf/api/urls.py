# Copyright The IETF Trust 2017, All Rights Reserved

from django.conf.urls import include

from ietf import api
from ietf.meeting import views as meeting_views
from ietf.submit import views as submit_views
from ietf.utils.urls import url

api.autodiscover()

urlpatterns = [
    # Top endpoint for Tastypie's REST API (this isn't standard Tastypie):
    url(r'^v1/?$', api.top_level),
    # Custom API endpoints
    url(r'^notify/meeting/import_recordings/(?P<number>[a-z0-9-]+)/?$', meeting_views.api_import_recordings),
    url(r'^submit/?$', submit_views.api_submit),
]
# Additional (standard) Tastypie endpoints
for n,a in api._api_list:
    urlpatterns += [
        url(r'^v1/', include(a.urls)),
    ]

