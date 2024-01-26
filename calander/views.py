from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import WeeklyFieldsMixin, DailyFieldsMixin
from .models import OneTimeEvent, RepetedEvent
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView
    )
# Create your views here.

class WeekEventsViewCreate(LoginRequiredMixin, WeeklyFieldsMixin, CreateView):
    model = RepetedEvent
    template_name = 'registration/weekly-create-update.html'
    
    def get_success_url(self):
        id = self.request.resolver_match.kwargs['pk']
        return reverse_lazy('calander:update_weekly', kwargs={'pk': id})  
    
    def get_context_data(self, **kwargs):
        ctx = super(WeekEventsViewCreate, self).get_context_data(**kwargs)
        ctx['button_text'] = 'ایجاد'
        return ctx
    
class WeekEventsViewUpdate(LoginRequiredMixin, WeeklyFieldsMixin, UpdateView):
    model = RepetedEvent
    template_name = 'registration/weekly-create-update.html'
    
    def get_success_url(self):
        id = self.request.resolver_match.kwargs['pk']
        return reverse_lazy('calander:update_weekly', kwargs={'pk': id})  

    def get_context_data(self, **kwargs):
        ctx = super(WeekEventsViewUpdate, self).get_context_data(**kwargs)
        ctx['button_text'] = 'ویرایش'
        return ctx

class OneEventCreate(LoginRequiredMixin, DailyFieldsMixin, CreateView):
    model = OneTimeEvent
    template_name = 'registration/day-create-update.html'

    def get_success_url(self):
        id = self.request.resolver_match.kwargs['pk']
        return reverse_lazy('calander:update_daily', kwargs={'pk': id})  
    
    def get_context_data(self, **kwargs):
        ctx = super(OneEventCreate, self).get_context_data(**kwargs)
        ctx['button_text'] = 'ایجاد'
        return ctx
        
class OneEventUpdate(LoginRequiredMixin, DailyFieldsMixin, UpdateView):
    model = OneTimeEvent
    template_name = 'registration/weekly-create-update.html'

    def get_success_url(self):
        id = self.request.resolver_match.kwargs['pk']
        return reverse_lazy('calander:update_daily', kwargs={'pk': id})  


    def get_context_data(self, **kwargs):
        ctx = super(OneEventUpdate, self).get_context_data(**kwargs)
        ctx['button_text'] = 'ویرایش'
        return ctx
