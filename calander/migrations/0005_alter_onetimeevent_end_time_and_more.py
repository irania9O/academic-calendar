# Generated by Django 5.0.1 on 2024-02-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calander', '0004_onetimeevent_owner_repetedevent_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimeevent',
            name='end_time',
            field=models.TimeField(default='14:32', help_text='زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:35', verbose_name='زمان پایان'),
        ),
        migrations.AlterField(
            model_name='onetimeevent',
            name='start_time',
            field=models.TimeField(default='14:32', help_text='زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:30', verbose_name='زمان شروع'),
        ),
        migrations.AlterField(
            model_name='repetedevent',
            name='end_time',
            field=models.TimeField(default='14:32', help_text='زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:35', verbose_name='زمان پایان'),
        ),
        migrations.AlterField(
            model_name='repetedevent',
            name='start_time',
            field=models.TimeField(default='14:32', help_text='زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:30', verbose_name='زمان شروع'),
        ),
    ]
