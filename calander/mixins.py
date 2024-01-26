from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from .models import RepetedEvent

class WeeklyFieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields = [
                'title', 'description', 
				'on_sunday', 'on_monday', 'on_tuesday', 'on_wednesday', 'on_thursday', 'on_friday', 'on_saturday',
				'event_type', 'half_year', 'start_time', 'end_time'
            ]
		return super().dispatch(request, *args, **kwargs)


class DailyFieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields = [
                'title', 'description', 
				'on_day',
				'start_time', 'end_time'
            ]
		return super().dispatch(request, *args, **kwargs)
