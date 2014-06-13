from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

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
	r = Results(poll=poll_id, choice=request.POST['choice'])
	r.save()
	# Always return an HttpResponseRedirect after successfully dealing
	# with POST data. This prevents data from being posted twice if a
	# user hits the Back button.
	#return HttpResponseRedirect(reverse('polls:results', args=(r.id,)))
	return render(request, 'polls/results.html', {'result': r})
