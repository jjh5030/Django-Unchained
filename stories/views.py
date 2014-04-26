from datetime import datetime

from django.http import HttpResponse
from stories.models import Story
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
	stories = top_stories(top=30)
	response = '''
	<!DOCTYPE html>

	<html>
		<head>
			<title>Tuts+ News</title>
		</head>

		<body>
			<ol>
				%s
			</ol>
		</body>
	</html>
	''' % '\n'.join(['<li>%s</li>' % story.title for story in stories])

	return HttpResponse(response)