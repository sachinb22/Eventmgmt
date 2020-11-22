from django.urls import path
from . import views

urlpatterns = [
	path('login',views.login,name='login'),
	path('joinus',views.joinus,name='joinus'),
	
	path('logout',views.logout,name='logout'),
	path('dashboard',views.dashboard,name='dashboard'),
	path('create_event',views.create_event,name='create_event')
	
	

]