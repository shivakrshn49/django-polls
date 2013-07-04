from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
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


# if settings.DEBUG:
# 	# urlpatterns += staticfiles_urlpatterns()
# 	urlpatterns += patterns('django.contrib.staticfiles.views', url(r'^static/(?P<path>.*)$', 'serve'),)
# else:	
# 	urlpatterns += patterns('',
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     )