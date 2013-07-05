"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import timezone
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from polls.models import Poll,Choice,Vote
from django.contrib.auth.models import User

class PollsAppTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="agiliq",email="admin@agiliq.com",password="admin")
        self.poll = Poll.objects.create(poll_user=self.user, question='wts up?',pub_date=timezone.localtime(timezone.now()))
        self.choice = Choice.objects.create(poll=self.poll,choice_text="Nothing Doing")

    def test_indexview(self):
        response = self.c.get(reverse("polls:index"))
        self.assertEqual(302, response.status_code)
        self.c.login(username="agiliq", password="admin")
        response = self.c.get(reverse("polls:index"))
        self.assertEqual(200, response.status_code)

    def test_detailview(self):
        response = self.c.get(reverse('polls:detail', args=[self.poll.id]))
        self.assertEqual(302, response.status_code)
        self.c.login(username="agiliq", password="admin")
        response = self.c.get(reverse('polls:detail', args=[self.poll.id]))
        self.assertEqual(200, response.status_code)


    def test_results(self):
        response = self.c.get(reverse('polls:results', args=[self.poll.id]))
        self.assertEqual(302, response.status_code)
        self.c.login(username="agiliq", password="admin")
        response = self.c.get(reverse('polls:results', args=[self.poll.id]))
        self.assertEqual(200, response.status_code)


    def test_vote(self):
        response = self.c.post(reverse('polls:vote', args=[self.poll.id]),{'choice':self.choice.id})
        self.assertEqual(302, response.status_code)
        self.c.login(username="agiliq", password="admin")
        response = self.c.post(reverse('polls:vote', args=[self.poll.id]), {'choice':self.choice.id})

    def test_created_voted_by_me(self):
        response = self.c.post(reverse('polls:polls_created_by_me'))
        self.assertEqual(302, response.status_code)
        self.c.login(username="agiliq", password="admin")
        response = self.c.post(reverse('polls:polls_created_by_me'))
        self.assertEqual(200, response.status_code)