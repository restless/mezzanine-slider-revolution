from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import settings
from mezzanine.core.fields import FileField, MultiChoiceField
from mezzanine.core.models import Orderable
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to
from slider_revolution.options import SlideOptions, CaptionOptions


@python_2_unicode_compatible
class Slider(models.Model):
    """
    A slider connected to a page
    """
    slug = models.SlugField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')

    def __str__(self):
        return self.slug


@python_2_unicode_compatible
class Slide(Orderable):
    """
    A slide in a slider
    """
    slider = models.ForeignKey(Slider, related_name="slides")
    image = FileField(verbose_name=_("Image"),
                      upload_to=upload_to('slider_revolution.Slide.image', 'sliders'),
                      format="Image", max_length=255, null=True, blank=True)

    # slide options
    transition = MultiChoiceField(max_length=500, choices=SlideOptions.TRANSITION_CHOICES, default=SlideOptions.BOXSLIDE)

    def __str__(self):
        return '{} | {}'.format(self.slider.slug, self.image)

    def image_thumb(self):
        return '<img src="{}{}" width="100" height="100" />'.format(settings.MEDIA_URL, self.image)
    image_thumb.allow_tags = True


@python_2_unicode_compatible
class SlideCaption(models.Model):
    slide = models.ForeignKey(Slide, related_name="captions")
    caption = models.CharField(max_length=200, null=True, blank=True)

    styling_caption = models.CharField(max_length=256, null=True, blank=True, help_text=_('It is the Wrapping main Class which is a MUST. Each Caption need to be defined like this, other way the Slider Plugin can not identifikate the Caption container'))
    incoming_animation = models.CharField(max_length=256, default=CaptionOptions.FADE, choices=CaptionOptions.INCOMING_ANIMATION_CLASSES_CHOICES, null=True, blank=True, help_text=_('Animation Classes defined the start / end animations on Captions'))
    outgoing_animation = models.CharField(max_length=256, default=CaptionOptions.FADEOUT, choices=CaptionOptions.OUTGOING_ANIMATION_CLASSES_CHOICES, null=True, blank=True, help_text=_('Animation Classes defined the start / end animations on Captions'))
    datax = models.CharField(max_length=256, default="300", null=True, blank=True, help_text=_('Possible Values are "left", "center", "right", or any Value between -2500 and 2500. If left/center/right is set, the caption will be siple aligned to the position. Any other "number" will simple set the left position in px of tha caption.'))
    datay = models.CharField(max_length=256, default="207", null=True, blank=True, help_text=_('Possible Values are "top", "center", "bottom", or any Value between -2500 and 2500. If top/center/bottom is set, the caption will be siple aligned to the position. Any other "number" will simple set the top position in px of tha caption.'))
    data_hoffset = models.CharField(max_length=256, default="", null=True, blank=True, help_text=_('Only works if data-x set to left/center/right. It will move the Caption with the defined "px" from the aligned position. i.e. data-x="center" data-hoffset="-100" will put the caption 100px left from the slide center horizontaly'))
    data_voffset = models.CharField(max_length=256, default="", null=True, blank=True, help_text=_('Only works if data-y set to top/center/bottom. It will move the Caption with the defined "px" from the aligned position. i.e. data-x="center" data-hoffset="-100" will put the caption 100px left from the slide center vertically.'))
    data_speed = models.CharField(max_length=256, default="300", null=True, blank=True, help_text=_('The speed in milliseconds of the transition to move the Caption in the Slide at the defined timepoint.'))
    data_start = models.CharField(max_length=256, default="800", null=True, blank=True, help_text=_('The timepoint in millisecond when/at the Caption should move in to the slide.'))
    data_endspeed = models.CharField(max_length=256, default="", null=True, blank=True, help_text=_('The speed in milliseconds of the transition to move the Caption out the Slide at the defined timepoint.'))
    data_end = models.CharField(max_length=256, default="", null=True, blank=True, help_text=_('The timepoint in millisecond when/at the Caption should move out from the slide.'))

    def __str__(self):
        return "{} | {}".format(self.slide, self.caption)
