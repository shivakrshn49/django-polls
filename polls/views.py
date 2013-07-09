from polls.models import Poll, Choice, Vote
from django.template import RequestContext, loader
from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.models import User


class IndexView(generic.ListView):
    login_required = True
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        # """Return the last five published polls."""
        # return Poll.objects.order_by('-pub_date')[:5]
        
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

 
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())
        
class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


class VoteClassBasedView(View):
    "This is a clased based view for above vote general view"

    # @method_decorator(login_required)
    def post(self, request,  poll_id=None, *args, **kwargs):
        p = get_object_or_404(Poll, pk=poll_id)
        # choice_objects_for_present_poll = p.choice_set.all()
        # for choice in choice_objects_for_present_poll:
        #     choice.votes = 0
        #     choice.save()
        try:
            selected_choice = p.choice_set.get(pk=request.POST['choice'])
            user = request.user
            try:
                voter = Vote.objects.get(user=user, poll=p)
                voter.choice = selected_choice
                voter.save()
            except Vote.DoesNotExist:
                vote = Vote.objects.create(user=user, poll=p,choice=selected_choice)
        except (KeyError, Choice.DoesNotExist):
            return render_to_response('polls/detail.html', {'poll': p, 'error_message': "You didn't select a choice."},context_instance=RequestContext(request))
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


@login_required
def created_voted_by_me(request):
    polls_by_loggedin_user = request.user.user_polls.all()
    polls_voted_by_loggedin_user = request.user.user_votes.all()
    return render_to_response('polls/created_voted_by_me.html', {'polls_by_loggedin_user': polls_by_loggedin_user, 'polls_voted_by_loggedin_user': polls_voted_by_loggedin_user},context_instance=RequestContext(request))
