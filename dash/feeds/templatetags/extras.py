from django import template
from django.template.defaultfilters import stringfilter

import re

register = template.Library()
p = re.compile('&amp;')
q = re.compile(r'<img.*?src=[\'"](.+?)[\'"].*?>')

@register.filter
@stringfilter
def imagify(value):
	matches = re.findall(q, value)
	z = []
	for m in matches:
		if not re.search(r'tweetmeme|share-button|~ff|add-to-any', m):
			z.append(m)
	if z:
		return z.pop(0)
