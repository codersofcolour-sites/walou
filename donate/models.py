from django.db import models
from wagtail.core.blocks.field_block import RichTextBlock
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel

class DonatePage(Page):

    donate_content = StreamField([
        ('subheading', blocks.RichTextBlock()),
        ('Description', blocks.RichTextBlock()),
        ('Donation_Details', blocks.RichTextBlock()),
    ], null = True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('donate_content')
    ]
