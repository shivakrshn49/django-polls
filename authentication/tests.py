"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from polls.models import Poll
from django.utils import timezone

class AuthenticationAppTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create(username='agiliq',email='admin@agiliq.com',password='admin')
        self.poll = Poll.objects.create(poll_user=self.user, question='wts up?',pub_date=timezone.localtime(timezone.now()))

    def test_loginview(self):
    	response = self.c.get(reverse('auth_required:login'))
    	self.assertEqual(200, response.status_code)
    	response = self.c.post(reverse('auth_required:login'),{'username':"agiliq", 'password':"admin", 'redirect_url': reverse('polls:results',args=[self.poll.id])})
    	self.assertEqual(200,response.status_code)


    def test_logout(self):
    	response = self.c.get(reverse('auth_required:logout'))
    	self.assertEqual(302,response.status_code)
