from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse


from .models import Topic, Post, Tag, Representation, PostVote, TagVote


def index(request):
	#return HttpResponse("Hello, world. You're at the agora index.")
	#'''
	#topic_list = Topic.objects
	#context = {'topic_list': topic_list}
	#return render(request, 'agora/index.html', context)
	return render(request, 'agora/index.html')


def topics(request, topic_id=None):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#return render(request, 'agora/detail.html', {'question': question})#
	#question = get_object_or_404(Question, pk=question_id)
	topic_list = Topic.objects.filter(parent=topic_id)
	context = {'topic_list': topic_list}
	if topic_id:
		current_topic = Topic.objects.get(id=topic_id)
		print dir(current_topic)
		context['current_topic'] = current_topic
		if current_topic.parent:
			context['parent_topic'] = current_topic.parent
		
	return render(request, 'agora/topics.html', context)

def posts(request, topic_id, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'agora/posts.html', {'post': post})
'''
def add_topic(request, topic_name, parent_id=None):
	#new_topic = Topic(
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'agora/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('agora:results', args=(p.id,)))
'''
