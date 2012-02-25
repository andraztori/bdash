from django.conf.urls.defaults import *
from django.views.generic.date_based import archive_index

from feedjack.models import Post, Link
from feeds.models import Category
from feeds.views import category_feed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feedjack_dict = {
	'queryset': Post.objects.all(), 
	'date_field': 'date_modified', 
	'template_name': 'index.html', 
	'num_latest': 50,
	'extra_context': { 'links': Link.objects.all, 'categories': Category.objects.all, },
}

urlpatterns = patterns('',
    # Example:
    # (r'^dash/', include('dash.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^news/', include('feedjack.urls')),
    (r'^edit/$', 'feeds.views.manage_categories'),
    (r'^edit/classify/$', 'feeds.views.classify'),
    (r'^(\w+)/$', 'feeds.views.category_index'),
    (r'^(\w+)/feed/$', category_feed()),
    (r'^$', 'django.views.generic.date_based.archive_index', feedjack_dict),
)
