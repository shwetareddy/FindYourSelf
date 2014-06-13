from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.sessions.backends.db import SessionStore
import datetime, time

from polls.models import Poll,Choice,Results

def index(request):
    latest_poll_list = Poll.objects.order_by('-question')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, r_id):
    return HttpResponse("You're looking at the results of poll.")

def vote(request, poll_id):
	if int(poll_id) == 1:
		now = datetime.datetime.now() 
		request.session['user_session'] = int(time.mktime(now.timetuple()))

	r = Results(user=request.session['user_session'], poll=poll_id, choice=request.POST['choice'])
	r.save()

	if int(poll_id) < 2 :
		next_poll_id = int(poll_id)+1
		return redirect('/polls/' + str(next_poll_id))
		#poll = Poll.objects.get(pk=next_poll_id)
		#return render(request, 'polls/detail.html', {'poll': poll})
	else:
		del request.session['user_session']
		return render(request, 'polls/results.html', {'result': r})
	
