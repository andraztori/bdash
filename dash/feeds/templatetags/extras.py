from django import template
from django.template.defaultfilters import stringfilter

import re

register = template.Library()

@register.filter
@stringfilter
def imagify(value):
	p = re.compile('&amp;')
	matches = re.findall(r'img src=[\'"]?([^\'" >]+)', value)
	if matches:
		return matches
