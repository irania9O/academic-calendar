from django.contrib import admin
from .models import HalfYear, OneTimeEvent, RepetedEvent

# Register your models here.

admin.site.register(HalfYear)
admin.site.register(OneTimeEvent)
admin.site.register(RepetedEvent)