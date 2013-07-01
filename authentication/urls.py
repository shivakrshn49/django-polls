from django.conf.urls import patterns, url
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from authentication.views import login_poll,logout_poll
# from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^login/$', login_poll, name='login'),
    url(r'^logout/$', logout_poll, name='logout'),
)