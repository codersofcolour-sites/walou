from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel 

@register_setting
class SocialMediaSettings(BaseSetting):
    """Social Media Settings for our custom website"""

    facebook = models.URLField(blank = True, null = True, help_text="Facebook Url")
    twitter = models.URLField(blank = True, null = True, help_text="Twitter Url")
    instagram = models.URLField(blank = True, null = True, help_text="Instagram Url")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("instagram"),

        ], heading = "Social Media Settings")
    ]

@register_setting(icon='image')
class WebsiteLogo(BaseSetting):
  website_logo = models.ForeignKey(
    "wagtailimages.Image",
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name="+",
  )

  panels = [
    ImageChooserPanel('website_logo'),
  ]

  class Meta:
    verbose_name = 'Website Logo'