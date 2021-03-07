
from __future__ import unicode_literals

from django.db import models
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


class AboutIndexPage(Page):
    pass

class AboutPage(Page):
    content = RichTextField(blank=True)
    side_image = models.ForeignKey(
      'wagtailimages.Image',
       null=True,
       blank=True,
       on_delete=models.SET_NULL,
       related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
        ImageChooserPanel('side_image'),
    ]