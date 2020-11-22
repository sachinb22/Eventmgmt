from django.urls import path
from . import views

urlpatterns = [
	path('',views.events,name='events'),
	path('<int:event_id>',views.event,name='event'),
	path('search',views.search,name='search'),

]