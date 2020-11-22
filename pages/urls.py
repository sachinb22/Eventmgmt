from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('categories',views.categories,name='categories'),
	path('create_event',views.create_event,name='create_event'),
	path('event_created',views.event_created,name='event_created'),
]