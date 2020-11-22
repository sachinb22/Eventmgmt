from django.shortcuts import render
from django.http import HttpResponse

from events.models import Event,UserEvent

# Create your views here.
def index(request):
	events = Event.objects.order_by('-list_date').filter(is_published=True)[:3]

	context = {
	   'events': events
	}

	return render(request,'pages/index.html',context)




def categories(request):
	return render(request,'pages/categories.html')


def create_event(request):
	return render(request,'pages/create_event.html')

def event_created(request):
	
	UserEvent.objects.create(
		title = request.POST['title'],
		address = request.POST['address'],
		venue =  request.POST['venue'],
		description = request.POST['description'],
		contact = request.POST['contact']
	)

	return render(request,'pages/index.html')