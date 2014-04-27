from datetime import datetime

from stories.models import Story
from stories.forms import StoryForm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.utils.timezone import utc

def score(story, gravity=1.8, timebase=120):
	points = (story.points - 1)**0.8
	now = datetime.utcnow().replace(tzinfo=utc)
	age = int((now - story.created_at).total_seconds())/60

	return points/(age+timebase)**gravity

def top_stories(top=180, consider=1000):
	latest_stories = Story.objects.all().order_by('-created_at')[:consider]
	rank_stories = sorted([(score(story), story) for story in latest_stories], reverse=True)

	return [story for _, story in rank_stories][:top]

def index(request):
	context_dict = {'stories': top_stories(top=30)}

	return render(request, 'hackernews/index.html', context_dict)

def story(request):
	if request.method == "POST":
		form = StoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = StoryForm()

	return render(request, 'hackernews/story.html', {'form': form})