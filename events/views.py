
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


from . models import Event

# Create your views here.
def events(request):
	events = Event.objects.order_by('-list_date')

	paginator = Paginator(events, 6)
	page = request.GET.get('page')
	paged_events = paginator.get_page(page)

	context = {
		'events': paged_events 
	}
	return render(request,'events/events.html', context)

def event(request, event_id):
	event = get_object_or_404(Event, pk=event_id)

	context = {
		'event':event
	}
	return render(request,'events/event.html',context)

def search(request):
	return render(request,'events/search.html')