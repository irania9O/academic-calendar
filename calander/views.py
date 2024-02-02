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
    
    def get_context_data(self, **kwargs):
        offset = int(self.request.resolver_match.kwargs['offset'])
        today = jdatetime.datetime.now().date() + jdatetime.timedelta(days=offset*7)
        days_to_subtract = today.weekday()
        first_day_of_week = today - jdatetime.timedelta(days=days_to_subtract)
        is_odd_week = first_day_of_week.day % 2 == 1

        ctx = super(WeekEventsViewList, self).get_context_data(**kwargs)
        ctx['is_half_year_selected'] = self.request.user.current_half_year != None
        ctx['first_day_of_week'] = first_day_of_week
        ctx['last_day_of_week'] = first_day_of_week + jdatetime.timedelta(days=6)
        ctx['next_week'] = reverse_lazy('calander:list_weekly', kwargs={'offset': offset + 1})
        ctx['previous_week'] = reverse_lazy('calander:list_weekly', kwargs={'offset': offset - 1})
        ctx['is_odd_week'] = is_odd_week
        return ctx

    def get_queryset(self):
        offset = int(self.request.resolver_match.kwargs['offset'])
        today = jdatetime.datetime.now().date() + jdatetime.timedelta(days=offset*7)
        days_to_subtract = today.weekday()
        first_day_of_week = today - jdatetime.timedelta(days=days_to_subtract)

        is_odd_week = first_day_of_week.day % 2 == 1

        start_date = first_day_of_week
        end_date = start_date + jdatetime.timedelta(days=6)
        
        datalist = []
        for event in RepetedEvent.objects.filter(owner=self.request.user, half_year=self.request.user.current_half_year):
            if event.event_type == 1:
                datalist.append(event)
            elif event.event_type == 2 and is_odd_week:
                datalist.append(event)
            elif event.event_type == 3 and not is_odd_week:
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

    def get_context_data(self, **kwargs):
        ctx = super(OneEventViewList, self).get_context_data(**kwargs)
        ctx['is_half_year_selected'] = self.request.user.current_half_year != None
        ctx['day'] = jdatetime.datetime.now().date() + jdatetime.timedelta(days=int(self.request.resolver_match.kwargs['offset']))
        ctx['next_day'] = reverse_lazy('calander:list_daily', kwargs={'offset': int(self.request.resolver_match.kwargs['offset']) + 1})
        ctx['previous_day'] = reverse_lazy('calander:list_daily', kwargs={'offset': int(self.request.resolver_match.kwargs['offset']) - 1})
        return ctx

    def get_queryset(self):
        offset = int(self.request.resolver_match.kwargs['offset'])
        today = jdatetime.datetime.now().date()
        day = today + jdatetime.timedelta(days=offset)
        days_to_subtract = (today.weekday()) % 7
        first_day_of_week = today - jdatetime.timedelta(days=days_to_subtract)

        is_odd_week = first_day_of_week.day % 2 == 1
        datalist = []

        onetime_events = OneTimeEvent.objects.filter(owner=self.request.user, on_day=day)
        for event in onetime_events:
            event.name_of_day()
            datalist.append(event)

        day = jdatetime.date.fromgregorian(date=day).weekday()

        if day == 0:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_friday=True, half_year=self.request.user.current_half_year)
        elif day == 1:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_saturday=True, half_year=self.request.user.current_half_year)
        elif day == 2:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_sunday=True, half_year=self.request.user.current_half_year)
        elif day == 3:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_monday=True, half_year=self.request.user.current_half_year)
        elif day == 4:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_tuesday=True, half_year=self.request.user.current_half_year)
        elif day == 5:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_wednesday=True, half_year=self.request.user.current_half_year)
        elif day == 6:
            repeat_events = RepetedEvent.objects.filter(owner=self.request.user, on_thursday=True, half_year=self.request.user.current_half_year)


        for event in repeat_events:
            if event.event_type == 1:
                datalist.append(event)
            elif event.event_type == 2 and is_odd_week:
                datalist.append(event)
            elif event.event_type == 3 and not is_odd_week:
                datalist.append(event)

        return datalist

class OneEventDelete(LoginRequiredMixin, DeleteView):
    model = OneTimeEvent
    template_name = 'registration/daily_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('calander:list_weekly', kwargs={'offset': 0})
