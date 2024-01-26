from django.contrib.auth import views
from django.urls import path
from .views import WeekEventsViewCreate, WeekEventsViewUpdate, OneEventCreate, OneEventUpdate, WeekEventsViewList, WeekEventsViewDelete, OneEventDelete,OneEventViewList

app_name = "calander"

urlpatterns = [
    path('weekly/create', WeekEventsViewCreate.as_view(), name='create_weekly'),
    path('weekly/<str:offset>', WeekEventsViewList.as_view(), name='list_weekly'),
    path('weekly/update/<int:pk>', WeekEventsViewUpdate.as_view(), name='update_weekly'),
    path('weekly/delete/<int:pk>', WeekEventsViewDelete.as_view(), name='delete_weekly'),

    path('day/create', OneEventCreate.as_view(), name='create_daily'),
    path('day/<str:offset>', OneEventViewList.as_view(), name='list_daily'),
    path('day/update/<int:pk>', OneEventUpdate.as_view(), name='update_daily'),
    path('day/delete/<int:pk>', OneEventDelete.as_view(), name='delete_daily'),
]