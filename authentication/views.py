from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from authentication.forms import LoginForm,RegistrationForm
from django.template import RequestContext
from django import forms


def login_poll(request):
    error_login = None
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
                else:
                    error_login = "Username or password does not match"
    return render_to_response("authentication/login.html", {'form': login_form, 'next': request.GET.get('next', ''),'errors':dict(login_form.errors.viewitems()),'error_login':error_login},
                              context_instance=RequestContext(request))    


def logout_poll(request):
	logout(request)
	return HttpResponseRedirect(reverse('auth_required:login'))

def register(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                                email=form.cleaned_data['email'], 
                                                password=form.cleaned_data['password1'])
            new_user.is_active = new_user.is_staff = True
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('polls:index'))
    return render_to_response('registration/registration_form.html',{'form':form,'errors':dict(form.errors.viewitems())},context_instance=RequestContext(request))