from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail_blocks.blocks import (
    HeaderBlock,
    ListBlock,
    ImageTextOverlayBlock,
    CroppedImagesWithTextBlock,
    ListWithImagesBlock,
    ThumbnailGalleryBlock,
    ChartBlock,
    MapBlock,
    ImageSliderBlock,
)
from wagtailstreamforms.blocks import WagtailFormBlock


class HomePage(Page):
    body = StreamField(
        [
            ("header", HeaderBlock()),
            ("list", ListBlock()),
            ("image_text_overlay", ImageTextOverlayBlock()),
            ("cropped_images_with_text", CroppedImagesWithTextBlock()),
            ("list_with_images", ListWithImagesBlock()),
            ("thumbnail_gallery", ThumbnailGalleryBlock()),
            ("chart", ChartBlock()),
            ("map", MapBlock()),
            ("image_slider", ImageSliderBlock()),
            ('form', WagtailFormBlock())
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
    ]
