from django.shortcuts import render
import pytz
from datetime import datetime

def world_clock(request):
    all_timezones = pytz.all_timezones  # Get ALL time zones
    selected_timezone = request.GET.get('timezone', 'UTC')  # Get user-selected timezone

    world_times = {
        tz: datetime.now(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S')
        for tz in ['UTC', 'America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney', selected_timezone]
    }

    return render(request, 'clock/world_clock.html', {'world_times': world_times, 'all_timezones': all_timezones})
