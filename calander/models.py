from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
import time
# print 

class HalfYear(models.Model):
    choices = [(1, 'اول'), (2, 'دوم')]
    defalut_year = jdatetime.datetime.now().year
    defalut_half = 1 if jdatetime.datetime.now().month <= 6 else 2
    year = models.IntegerField(verbose_name="سال", blank=False, null=False, choices=[(i, i) for i in range(1400, 1420)], default=defalut_year)
    half = models.IntegerField(verbose_name="نیمسال", choices=choices, blank=False, null=False, default=defalut_half)

    class Meta:
        unique_together = ('year', 'half')
        verbose_name = "نیمسال"
        verbose_name_plural = "نیمسال ها"
        
    def __str__(self):
        return 'نیم سال ' + str(self.choices[self.half - 1][1]) + " " + str(self.year) 

class RepetedEvent(models.Model):
    objects = jmodels.jManager()
    today = jdatetime.datetime.now().date()
    format_date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="مالک", blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    
    on_saturday = models.BooleanField(verbose_name="شنبه", default=False)
    on_sunday = models.BooleanField(verbose_name="یکشنبه", default=False)
    on_monday = models.BooleanField(verbose_name="دوشنبه", default=False)
    on_tuesday = models.BooleanField(verbose_name="سه شنبه", default=False)
    on_wednesday = models.BooleanField(verbose_name="چهارشنبه", default=False)
    on_thursday = models.BooleanField(verbose_name="پنجشنبه", default=False)
    on_friday = models.BooleanField(verbose_name="جمعه", default=False)

    event_type = models.IntegerField(verbose_name="نوع ایونت", choices=[(1, 'معمولی'), (2, 'هفته ی فرد'), (3, 'هفته ی زوج')], default=1)
    half_year = models.ForeignKey(HalfYear, on_delete=models.CASCADE, default=None, verbose_name="نیمسال")
    start_time = models.TimeField(verbose_name="زمان شروع", help_text="زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:30", default=time.strftime("%H:%M"))
    end_time = models.TimeField(verbose_name="زمان پایان", help_text="زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:35", default=time.strftime("%H:%M"))


    class Meta:
        verbose_name = "رویداد تکراری"
        verbose_name_plural = "رویداد های تکراری"

    def __str__(self):
        return self.title + ' ' + str(self.half_year) + ' ' + str(self.start_time) + ' ' + str(self.end_time)
    
    def get_week_day_names(self):
        days = []
        if self.on_saturday:
            days.append('شنبه')
        if self.on_sunday:
            days.append('یکشنبه')
        if self.on_monday:
            days.append('دوشنبه')
        if self.on_tuesday:
            days.append('سه شنبه')
        if self.on_wednesday:
            days.append('چهارشنبه')
        if self.on_thursday:
            days.append('پنجشنبه')
        if self.on_friday:
            days.append('جمعه')
        return days
    

class OneTimeEvent(models.Model):
    objects = jmodels.jManager()
    today = jdatetime.datetime.now().date()
    format_date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="مالک", blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    on_day = jmodels.jDateField(verbose_name="روز", help_text="تاریخ را به فرمت سال-ماه-روز وارد کنید. مثال: <br>" + format_date, default=format_date)
    start_time = models.TimeField(verbose_name="زمان شروع", help_text="زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:30", default=time.strftime("%H:%M"))
    end_time = models.TimeField(verbose_name="زمان پایان", help_text="زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:35", default=time.strftime("%H:%M"))

    class Meta:
        verbose_name = "رویداد یک بار"
        verbose_name_plural = "رویداد های یک بار"

    def __str__(self):
        return self.title + ' ' + str(self.on_day) + ' ' + str(self.start_time) + ' ' + str(self.end_time)
    
    def name_of_day(self):
        day = jdatetime.date.fromgregorian(date=self.on_day).weekday()
        self.on_time = True

        if day == 0:
            self.on_friday = True
        elif day == 1:
            self.on_saturday = True
        elif day == 2:
            self.on_sunday = True
        elif day == 3:
            self.on_monday = True
        elif day == 4:
            self.on_tuesday = True
        elif day == 5:
            self.on_wednesday = True
        elif day == 6:
            self.on_thursday = True

    def get_week_day_name(self):
        day = jdatetime.date.fromgregorian(date=self.on_day).weekday()
        if day == 1:
            return 'شنبه'
        elif day == 2:
            return 'یکشنبه'
        elif day == 3:
            return 'دوشنبه'
        elif day == 4:
            return 'سه شنبه'
        elif day == 5:
            return 'چهارشنبه'
        elif day == 6:
            return 'پنجشنبه'
        elif day == 0:
            return 'جمعه'