from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from datetime import datetime, timedelta
from books.models import Publisher, Book


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


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = dict()

    html['request.GET'] = request.GET
    html['request.POST'] = request.POST
    html['request.path'] = request.path

    for k, v in values:
        html[k] = v

    return render(request, 'meta.html', {'data': html})


# generic splitter method for all views that involve get/post
def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)

    if request.method == 'GET' and get_view:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view:
        return post_view(request, *args, **kwargs)

    raise Http404


# subclass ListView
class JJListView(ListView):
    template_name = 'showList.html'
    name = 'DEFAULT NAME :('

    def get_context_data(self, **kwargs):
        # call base
        context = super(JJListView, self).get_context_data(**kwargs)

        # add name
        context['name'] = self.name

        return context


class JJDPublisheretailView(DetailView):
    model = Publisher
    template_name = 'publisher.html'

    def get_context_data(self, **kwargs):
        context = super(JJDPublisheretailView, self).get_context_data(**kwargs)

        context['book_list'] = Book.objects.filter(publisher = publisher)

        return context