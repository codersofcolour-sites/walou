from django.db import models
from modelcluster.fields import ParentalKey 

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock



class HomePageCarouselImages(Orderable):

    page = ParentalKey("home.HomePage", related_name = "carousel_images")

    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null= True,
        blank = False,
        on_delete= models.SET_NULL,
        related_name= "+"
    )

    panels = [
        ImageChooserPanel("carousel_image"),
    ]

class HomePage(Page):
    """Home page model"""
    
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            InlinePanel("carousel_images"),
        ], heading ="Carousel Images"),

        FieldPanel('body', classname="full"),
        
        
    ]