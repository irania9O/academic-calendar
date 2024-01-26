from django.contrib.auth import views
from django.urls import path
from .views import WeekEventsViewCreate, WeekEventsViewUpdate, OneEventCreate, OneEventUpdate

app_name = "calander"

urlpatterns = [
    path('weekly/create', WeekEventsViewCreate.as_view(), name='create_weekly'),
    path('weekly/update/<int:pk>', WeekEventsViewUpdate.as_view(), name='update_weekly'),
    path('day/create', OneEventCreate.as_view(), name='create_daily'),
    path('day/update/<int:pk>', OneEventUpdate.as_view(), name='update_daily'),
]