from django.db import models 

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock



class HomePage(Page):
    """Home page model"""

    banner_title = models.CharField(max_length=100, blank = True, null = True)
    banner_subtitle = RichTextField(blank = True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null= True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name= "+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null= True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name= "+"
    )

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        FieldPanel('body', classname="full"),
        PageChooserPanel("banner_cta"),
        
    ]