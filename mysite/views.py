from django.http import HttpResponse, Http404
from django.shortcuts import render
from datetime import datetime, timedelta


def hello(request):
    return HttpResponse("Hello world.")


def current_datetime(request):
    now = datetime.now()

    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.now() + timedelta(hours=offset)

    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})
