# Generated by Django 5.0.1 on 2024-02-02 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calander', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepetedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('on_saturday', models.BooleanField(default=False, verbose_name='شنبه')),
                ('on_sunday', models.BooleanField(default=False, verbose_name='یکشنبه')),
                ('on_monday', models.BooleanField(default=False, verbose_name='دوشنبه')),
                ('on_tuesday', models.BooleanField(default=False, verbose_name='سه شنبه')),
                ('on_wednesday', models.BooleanField(default=False, verbose_name='چهارشنبه')),
                ('on_thursday', models.BooleanField(default=False, verbose_name='پنجشنبه')),
                ('on_friday', models.BooleanField(default=False, verbose_name='جمعه')),
                ('event_type', models.IntegerField(choices=[(1, 'معمولی'), (2, 'هفته ی فرد'), (3, 'هفته ی زوج')], default=1, verbose_name='نوع ایونت')),
                ('start_time', models.TimeField(default='14:31', help_text='زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:30', verbose_name='زمان شروع')),
                ('end_time', models.TimeField(default='14:31', help_text='زمان را به فرمت ساعت:دقیقه وارد کنید. مثال: <br> 12:35', verbose_name='زمان پایان')),
                ('half_year', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='calander.halfyear', verbose_name='نیمسال')),
            ],
            options={
                'verbose_name': 'رویداد تکراری',
                'verbose_name_plural': 'رویداد های تکراری',
            },
        ),
    ]
