from __future__ import unicode_literals
from mezzanine import template
from mezzanine.conf import settings
from ..models import Slider

register = template.Library()

@register.inclusion_tag("slider_revolution/slider.html", takes_context=True)
def slider(context, slug):
    """
    Renders a slider.
    """
    slider = Slider.objects.get(slug=slug)
    settings.use_editable()
    slides = slider.slides.all()
    context['slider'] = slider
    context['slides'] = slides
    return context


@register.inclusion_tag("slider_revolution/slider_js_media.html", takes_context=True)
def slider_js_media(context, slug):
    """
    Renders a slider js media.
    """
    context['slider_id'] = '#{}'.format(slug)
    return context


@register.inclusion_tag("slider_revolution/slider_css_media.html", takes_context=True)
def slider_css_media(context, slug):
    """
    Renders a slider css media.
    """
    context['slider_id'] = '#{}'.format(slug)
    return context