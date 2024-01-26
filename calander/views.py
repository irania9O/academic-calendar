from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import WeeklyFieldsMixin, DailyFieldsMixin
from .models import OneTimeEvent, RepetedEvent
from django.urls import reverse_lazy
import jdatetime

from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView
    )

weekdaysـfa = ['جمعه', 'شنبه', 'یکشنبه', 'دوشنبه', 'سه شنبه', 'چهارشنبه', 'پنجشنبه']
weekdays_en = ['friday', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday']
# Create your views here.

class WeekEventsViewCreate(LoginRequiredMixin, WeeklyFieldsMixin, CreateView):
    model = RepetedEvent
    template_name = 'registration/weekly-create-update.html'
    
    def get_success_url(self):
        # id = self.request.resolver_match.kwargs['pk']
        return reverse_lazy('calander:list_weekly', kwargs={'offset': 0})
    
    def get_context_data(self, **kwargs):
        ctx = super(WeekEventsViewCreate, self).get_context_data(**kwargs)
        ctx['button_text'] = 'ایجاد'
        return ctx
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class WeekEventsViewUpdate(LoginRequiredMixin, WeeklyFieldsMixin, UpdateView):
    model = RepetedEvent
    template_name = 'registration/weekly-create-update.html'
    
    def get_success_url(self):
        return reverse_lazy('calander:list_weekly', kwargs={'offset': 0})

    def get_context_data(self, **kwargs):
        ctx = super(WeekEventsViewUpdate, self).get_context_data(**kwargs)
        ctx['button_text'] = 'ویرایش'
        return ctx

class WeekEventsViewList(LoginRequiredMixin, ListView):
    model = RepetedEvent
    template_name = 'registration/weekly.html'
    # context_object_name = 'events'

    def get_queryset(self):
        offset = int(self.request.resolver_match.kwargs['offset'])
        today = jdatetime.datetime.now().date() + jdatetime.timedelta(days=offset*7)
        days_to_subtract = (today.weekday()) % 7
        first_day_of_week = today - jdatetime.timedelta(days=days_to_subtract)

        start_date = first_day_of_week
        end_date = start_date + jdatetime.timedelta(days=6)
        print(start_date, end_date)
        datalist = []
        for event in RepetedEvent.objects.filter(owner=self.request.user):
            datalist.append(event)

        repeat_events = OneTimeEvent.objects.filter(owner=self.request.user, on_day__range=[start_date, end_date])
        for event in repeat_events:
            event.name_of_day()
            datalist.append(event)
        return datalist
    
class WeekEventsViewDelete(LoginRequiredMixin, DeleteView):
    model = RepetedEvent
    template_name = 'registration/weekly_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('calander:list_weekly', kwargs={'offset': 0})

class OneEventCreate(LoginRequiredMixin, DailyFieldsMixin, CreateView):
    model = OneTimeEvent
    template_name = 'registration/daily-create-update.html'

    def get_success_url(self):
        return reverse_lazy('calander:list_weekly', kwargs={'offset': 0})
    
    def get_context_data(self, **kwargs):
        ctx = super(OneEventCreate, self).get_context_data(**kwargs)
        ctx['button_text'] = 'ایجاد'
        return ctx

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        
class OneEventUpdate(LoginRequiredMixin, DailyFieldsMixin, UpdateView):
    model = OneTimeEvent
    template_name = 'registration/daily-create-update.html'

    def get_success_url(self):
        id = self.request.resolver_match.kwargs['pk']
        return reverse_lazy('calander:update_daily', kwargs={'pk': id})  


    def get_context_data(self, **kwargs):
        ctx = super(OneEventUpdate, self).get_context_data(**kwargs)
        ctx['button_text'] = 'ویرایش'
        return ctx


class OneEventViewList(LoginRequiredMixin, ListView):
    model = RepetedEvent
    template_name = 'registration/daily.html'
    # context_object_name = 'events'

    def get_queryset(self):
        offset = int(self.request.resolver_match.kwargs['offset'])
        today = jdatetime.datetime.now().date()
        day = today + jdatetime.timedelta(days=offset)
        datalist = []

        onetime_events = OneTimeEvent.objects.filter(owner=self.request.user, on_day=day)
        for event in onetime_events:
            event.name_of_day()
            datalist.append(event)

        day = jdatetime.date.fromgregorian(date=today).weekday()
        if day == 0:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_friday=True)
        elif day == 1:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_saturday=True)
        elif day == 2:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_sunday=True)
        elif day == 3:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_monday=True)
        elif day == 4:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_tuesday=True)
        elif day == 5:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_wednesday=True)
        elif day == 6:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_thursday=True)
        
        for event in repeat_events:
            datalist.append(event)

        return datalist

class OneEventDelete(LoginRequiredMixin, DeleteView):
    model = OneTimeEvent
    template_name = 'registration/daily_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('calander:list_weekly', kwargs={'offset': 0})
