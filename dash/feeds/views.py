from django.shortcuts import get_object_or_404, render_to_response, HttpResponseRedirect
from feedjack.models import Post, Link
from feeds.models import Infographic, Category, Source
from django.template import Context, loader
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from feeds.templatetags.extras import imagify

class category_feed(Feed):
    def get_object(self, request, cat):
        return get_object_or_404(Category, slug=cat)

    def title(self, obj):
        return "news in pictures: %s" % obj.title

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return "news %s" % obj.title
        
    def items(self, obj):
        return Infographic.objects.filter(category__slug__exact=obj.slug)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

def category_index(request, cat):
	# show last 100 Infographics with Category set
	c = Category.objects.get(slug=cat)
	cc = c.infographic_set;
	return render_to_response('index2.html', {
		'latest': cc.order_by('source__date_modified').reverse(), 
		'links': Link.objects.all(), 
		'categories': Category.objects.all(),
		'selected': c,
	})
    
def manage_categories(request):
	# show the first two Posts that doesn't have corresponding Infographic pairs yet.
    return render_to_response('edit.html', {
    	'latest': Post.objects.filter(infographic__isnull=True)[0:1], 
    	'links': Link.objects.all(), 
		'categories': Category.objects.all(),
    }, context_instance=RequestContext(request))

def classify(request):
    p = get_object_or_404(Post, guid=request.POST['guid'])
    try:
        selected_choice = Category.objects.get(title=request.POST['category'])
    except (KeyError, Category.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('edit.html', {
            'error_message': "You didn't select a choice.",
            'latest': Post.objects.filter(infographic__title__isnull=True)[0:2],
            'categories': Category.objects.all(),
        }, context_instance=RequestContext(request))
    else:
    	image = imagify(p.content)
        i = Infographic(title=p.title, source=p, category=selected_choice, url=p.link, text=p.content, imageurl=image)
        i.save()
        return HttpResponseRedirect(reverse('feeds.views.manage_categories'))
