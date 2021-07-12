from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
    AbstractFormField
)

# Create your models here.
class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"

    intro = RichTextField(blank = True)
    thank_you_text = RichTextField(blank = True)
    
    contact_content = StreamField([
        ('subheading', blocks.RichTextBlock()),        
    ], null = True)

    content_panels = AbstractEmailForm.content_panels + [
        StreamFieldPanel('contact_content'),      
        FieldPanel('intro'),
        InlinePanel('form_fields', label ='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname = "col6"),
                FieldPanel('to_address', classname = "col6"),
            ]),
            FieldPanel("subject"),
        ], heading = "Email Settings"),
        
    ]
