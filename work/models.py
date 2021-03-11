from __future__ import unicode_literals

from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel)
from modelcluster.fields import ParentalKey

# Create your models here.
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from work import blocks
from wagtail.core import blocks as work_blocks
from wagtail.search import index


class WorkIndexPage(Page):
    pass

class FullStackPage(Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
    ]

class TechnologyDetailOrderable(Orderable):
    page = ParentalKey("work.TechnologyPage", related_name="technologypage")
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True)

class TechnologyPage(Page):

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('technologypage'),
        ], heading="Technology or Framework details"),
    ]
