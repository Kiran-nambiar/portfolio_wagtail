
from __future__ import unicode_literals

from django.db import models
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel, InlinePanel)
from modelcluster.fields import ParentalKey

# Create your models here.
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


class DeveloperLogo(Orderable):
    page = ParentalKey("about.AboutPage", related_name="aboutpage")
    development_logo = models.ForeignKey(
      'wagtailimages.Image',
       null=True,
       blank=True,
       on_delete=models.SET_NULL,
       related_name='+'
    )

    panels = [
        ImageChooserPanel("development_logo")
    ]

class AboutPage(Page):
    content = RichTextField(blank=True)
    side_image = models.ForeignKey(
      'wagtailimages.Image',
       null=True,
       blank=True,
       on_delete=models.SET_NULL,
       related_name='+'
    )
    developer_title = models.CharField(max_length=255, null=True)
    developer_intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
        ImageChooserPanel('side_image'),
        FieldPanel('developer_title', classname="full"),
        FieldPanel('developer_intro', classname="full"),
        MultiFieldPanel(
            [
                InlinePanel("aboutpage")
            ],
            heading="Development logos",
        )
    ]