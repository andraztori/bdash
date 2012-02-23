from django.conf.urls.defaults import *
from django.views.generic.date_based import archive_index

from feedjack.models import Post, Link
from feeds.templatetags.extras import imagify

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feedjack_dict = {
	'queryset': Post.objects.all(), 
	'date_field': 'date_modified', 
	'template_name': 'index.html', 
	'num_latest': 100,
	'extra_context': { 'links': Link.objects.all, },
}

urlpatterns = patterns('',
    # Example:
    # (r'^dash/', include('dash.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^news/', include('feedjack.urls')),
    (r'^$', 'django.views.generic.date_based.archive_index', feedjack_dict),
)
