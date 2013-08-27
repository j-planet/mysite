from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
import contact.views

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

# mysite stuff
urlpatterns = patterns('mysite.views',
                       url(r'^hello/$', 'hello'),
                       url(r'^time/$', 'current_datetime'),
                       url(r'^time/plus/(?P<offset>\d{1,2})/$', 'hours_ahead'),)
# books stuff
urlpatterns += patterns('books.views',
                        url(r'^search/$', 'search'),)

# contact stuff
urlpatterns += patterns('',
                        url(r'^contact/$', 'mysite.views.method_splitter',
                            {'GET': contact.views.contact_get, 'POST': contact.views.contact_post}),
                        url(r'^contact/thanks/$', 'contact.views.thanks'),)

# default django stuff
urlpatterns += patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^mysite/', include('mysite.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),)

# debug stuff
if settings.DEBUG:
    urlpatterns += patterns('mysite.views',
                           url(r'^meta/$', 'display_meta'),)