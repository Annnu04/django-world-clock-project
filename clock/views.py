from django.shortcuts import render
import pytz
from datetime import datetime

def world_clock(request):
    timezones = ['UTC', 'America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']
    world_times = {tz: datetime.now(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S') for tz in timezones}
    
    return render(request, 'clock/world_clock.html', {'world_times': world_times})
