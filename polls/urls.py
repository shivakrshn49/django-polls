from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from polls import views


urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>\d+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', login_required(views.ResultsView.as_view()), name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<poll_id>\d+)/vote/$', login_required(views.VoteClassBasedView.as_view()), name='vote'),
    # url(r'^(?P<pk>\d+)/$', views.created_voted_by_me, name='authentication_required')
)