from django.conf.urls import patterns, include, url
from polls.views import VoteClassBasedView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^polls/', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('authentication.urls',namespace="auth_required")),
)
