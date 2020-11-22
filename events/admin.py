from django.contrib import admin

# Register your models here.
from . models import Event,UserEvent

class EventAdmin(admin.ModelAdmin):
	list_display = ( 'id', 'title', 'is_published', 'ticketprice', 'list_date')
	list_display_links = ('id', 'title')
	list_editable = ('is_published',)
	search_fields = ('title','description','address','ticketprice',)
	list_per_page = 25

admin.site.register(Event, EventAdmin)
admin.site.register(UserEvent)