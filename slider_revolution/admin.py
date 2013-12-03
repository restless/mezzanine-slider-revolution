from __future__ import unicode_literals

from django.contrib import admin
from django.core import urlresolvers
from mezzanine.core.admin import TabularDynamicInlineAdmin, StackedDynamicInlineAdmin

from slider_revolution.models import Slider, SlideCaption, Slide


class SlideInline(TabularDynamicInlineAdmin):
    template = "slider_revolution/admin/slide_dynamic_inline_tabular.html"
    model = Slide
    extra = 1

    def changeform_link(self, instance):
        if instance.id:
            changeform_url = urlresolvers.reverse('admin:slider_revolution_slide_change', args=(instance.id,))
            return '<a href="{}">Details</a>'.format(changeform_url)
        else:
            addform_url = urlresolvers.reverse('admin:slider_revolution_slide_add')
            return '<a href="{}">Add</a>'.format(addform_url)
        return u''

    changeform_link.allow_tags = True
    changeform_link.short_description = 'Slide'
    fields = ("image_thumb", "changeform_link")
    readonly_fields = ("image_thumb", "changeform_link",)


class SliderAdmin(admin.ModelAdmin):
    inlines = (SlideInline,)


class SlideCaptionInline(StackedDynamicInlineAdmin):
    model = SlideCaption


class SlideAdmin(admin.ModelAdmin):
    inlines = (SlideCaptionInline,)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Slide, SlideAdmin)
