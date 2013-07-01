from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from authentication.forms import LoginForm
from django.template import RequestContext


def login_poll(request):
    login_form = LoginForm()
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('polls:index'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
        	user = authenticate(username=username, password=password)
        	if user is not None:
        		if user.is_active:
        			login(request, user)
                	return HttpResponseRedirect(reverse('polls:index'))
    return render_to_response("authentication/login.html", {'form': login_form, 'next': request.GET.get('next', '')},
                              context_instance=RequestContext(request))    


def logout_poll(request):
	logout(request)
	return HttpResponseRedirect(reverse('auth_required:login'))
