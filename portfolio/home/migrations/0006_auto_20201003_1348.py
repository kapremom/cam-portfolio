# Generated by Django 3.1.2 on 2020-10-03 17:48

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_resumepage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "header",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "header",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("h1", "H1"),
                                            ("h2", "H2"),
                                            ("h3", "H3"),
                                            ("h4", "H4"),
                                            ("h5", "H5"),
                                            ("h6", "H6"),
                                        ],
                                        label="Header Size",
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.core.blocks.CharBlock(
                                        label="Text", max_length=50
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "list",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "content",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.CharBlock(), label="Items"
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "image_text_overlay",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Image"
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.core.blocks.CharBlock(
                                        label="Text", max_length=200
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "cropped_images_with_text",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "image_items",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        label="Image"
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.core.blocks.CharBlock(
                                                        label="Text", max_length=200
                                                    ),
                                                ),
                                            ]
                                        ),
                                        label="Image Item",
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "list_with_images",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "list_items",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        label="Image"
                                                    ),
                                                ),
                                                (
                                                    "title",
                                                    wagtail.core.blocks.CharBlock(
                                                        label="Title", max_length=200
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.core.blocks.CharBlock(
                                                        label="Text", max_length=200
                                                    ),
                                                ),
                                                (
                                                    "link_text",
                                                    wagtail.core.blocks.CharBlock(
                                                        label="Link Text",
                                                        max_length=200,
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "link_url",
                                                    wagtail.core.blocks.URLBlock(
                                                        label="Link URL",
                                                        max_length=200,
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        ),
                                        label="List Item",
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "thumbnail_gallery",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "image_items",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        label="Image"
                                                    ),
                                                )
                                            ]
                                        ),
                                        label="Image",
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "chart",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(
                                        default="Chart Title",
                                        label="Title",
                                        max_length=120,
                                    ),
                                ),
                                (
                                    "chart_type",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("bar", "Bar"),
                                            ("horizontalBar", "Horizontal Bar"),
                                            ("pie", "Pie"),
                                            ("doughnut", "Doughnut"),
                                            ("polarArea", "Polar Area"),
                                            ("radar", "Radar"),
                                            ("line", "Line"),
                                        ],
                                        label="Chart Type",
                                    ),
                                ),
                                (
                                    "labels",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.CharBlock(
                                            default="Label",
                                            label="Label",
                                            max_length=40,
                                        ),
                                        label="Chart Labels",
                                    ),
                                ),
                                (
                                    "datasets",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "label",
                                                    wagtail.core.blocks.CharBlock(
                                                        default="Dataset #1",
                                                        label="Dataset Label",
                                                        max_length=120,
                                                    ),
                                                ),
                                                (
                                                    "dataset_data",
                                                    wagtail.core.blocks.ListBlock(
                                                        wagtail.core.blocks.IntegerBlock(),
                                                        default="0",
                                                        label="Data",
                                                    ),
                                                ),
                                            ]
                                        ),
                                        label="Dataset",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "map",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "marker_title",
                                    wagtail.core.blocks.CharBlock(
                                        default="Marker Title 'This will be updated after you save changes.'",
                                        max_length=120,
                                    ),
                                ),
                                (
                                    "marker_description",
                                    wagtail.core.blocks.RichTextBlock(),
                                ),
                                (
                                    "zoom_level",
                                    wagtail.core.blocks.IntegerBlock(
                                        default="2",
                                        max_value=18,
                                        min_value=0,
                                        required=False,
                                    ),
                                ),
                                (
                                    "location_x",
                                    wagtail.core.blocks.FloatBlock(
                                        default="35.0", required=False
                                    ),
                                ),
                                (
                                    "location_y",
                                    wagtail.core.blocks.FloatBlock(
                                        default="0.16", required=False
                                    ),
                                ),
                                (
                                    "marker_x",
                                    wagtail.core.blocks.FloatBlock(
                                        default="51.5", required=False
                                    ),
                                ),
                                (
                                    "marker_y",
                                    wagtail.core.blocks.FloatBlock(
                                        default="-0.09", required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "image_slider",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "image_items",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        label="Image"
                                                    ),
                                                )
                                            ]
                                        ),
                                        label="Image",
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "form",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("form", wagtailstreamforms.blocks.FormChooserBlock()),
                                (
                                    "form_action",
                                    wagtail.core.blocks.CharBlock(
                                        help_text='The form post action. "" or "." for the current page or a url',
                                        required=False,
                                    ),
                                ),
                                (
                                    "form_reference",
                                    wagtailstreamforms.blocks.InfoBlock(
                                        help_text="This form will be given a unique reference once saved",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "Parallax",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.core.blocks.RichTextBlock(
                                        help_text="Text to overlay parallax",
                                        required=False,
                                    ),
                                ),
                                (
                                    "img",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Image for parallax", required=True
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "Code",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("css", "CSS"),
                                            ("diff", "diff"),
                                            ("html", "HTML"),
                                            ("javascript", "Javascript"),
                                            ("json", "JSON"),
                                            ("python", "Python"),
                                            ("scss", "SCSS"),
                                            ("yaml", "YAML"),
                                        ],
                                        help_text="Coding language",
                                        identifier="language",
                                        label="Language",
                                    ),
                                ),
                                (
                                    "code",
                                    wagtail.core.blocks.TextBlock(
                                        identifier="code", label="Code"
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
    ]
