from __future__ import unicode_literals

from django.db import models
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey
# Create your models here.
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel, InlinePanel)
from wagtail.search import index
from wagtail.snippets.models import register_snippet

class HomeIndexPage(Page):
    pass

class HomeSelectionOrderable(Orderable):
    page = ParentalKey("home.HomePage", related_name="homepage")
    selection_title = models.CharField(max_length=255)
    selection_handle = models.CharField(max_length=255)

class HomePage(Page):
    side_image = models.ForeignKey(
      'wagtailimages.Image',
       null=True,
       blank=True,
       on_delete=models.SET_NULL,
       related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('side_image'),
        MultiFieldPanel(
            [
                InlinePanel("homepage", label="Home Selection")
            ],
            heading="Homepage Selection",
            classname="collapsible collapsed",
        )
    ]

