from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.blocks import ListBlock

from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import URLBlock
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailcore.blocks import ChoiceBlock
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailimages import blocks


class StandardParagraphBlock(StructBlock):

    headline = CharBlock(required=False, length=256)
    text = RichTextBlock(required=True)

    class Meta:
        template = 'blocks/block_standard_paragraph.html'
        icon = 'pilcrow'
        label = 'Basic Paragraph'
        help_text = 'Basic text paragraph with optional heading.'



class HighlightParagraphBlock(StructBlock):

    headline = CharBlock(required=False, length=256)
    text = RichTextBlock(required=True)
    link = PageChooserBlock(required=False)

    class Meta:
        template = 'blocks/block_highlight_paragraph.html'
        icon = 'pilcrow'
        label = 'Gray Paragraph'
        help_text = 'Paragraph with gray background and optional single link.'



# class QuoteParagraph(StructBlock):

#     text = RichTextBlock(required=True)
#     color = ChoiceBlock(
#                 choices=[('green','Gruen'),('orange','Orange'),('red','Rot')],
#                 required=True,
#                 help_text="Select a color from the list."
#             )
#     author = CharBlock(required=False, length=256)

#     class Meta:
#         template="blocks/block_quote_paragraph_image.html",
#         icon="pilcrow",
#         help_text="Centered text (set quotemarks manually) with background color and optional author field."


class QuoteParagraph(StructBlock):

    text = RichTextBlock(required=True)
    color = ChoiceBlock(
                choices=[('green','Gruen'),('orange','Orange'),('red','Rot')],
                required=False,
                help_text="Select a color from the list."
            )
    image = ImageChooserBlock(
                required=False,
                help_text="Please use an image with at least 800x400px or a similar aspect ratio."
            )
    author = CharBlock(required=False, length=256)

    class Meta:
        template="blocks/block_quote_paragraph_image.html",
        icon="pilcrow",
        help_text="Centered text (set quotemarks manually) with background color or background image and optional author field."



class ColumnBlock(StructBlock):

    col1_headline = CharBlock(required=False, length=256)
    col1_text = RichTextBlock(required=True)
    col2_headline = CharBlock(required=False, length=256)
    col2_text = RichTextBlock(required=True)

    class Meta:
        template = 'blocks/block_column.html'
        icon = 'grip'
        label = '2 Column Text'
        help_text = 'Text in 2 columns with optional column heading.'



class ImageSliderBlock(ListBlock):

    ImageChooserBlock(
        label = 'Image',
        help_text = 'Images will be used with a 950x450px size.'
    )

    class Meta:
        template = 'blocks/block_carousel.html'
        icon = 'image'
        label = 'Image Slider'
        help_text = 'Responsive image slider (weipe on mobile). Please choose 4 images.'



class LinkboxBlock(StructBlock):

    headline = CharBlock(required=False, length=256)
    text = RichTextBlock(required=False)
    links = ListBlock(
                PageChooserBlock(),
            )

    class Meta:
        template = 'blocks/block_linkbox.html'
        icon = 'link'
        label = 'Link Box'
        help_text = 'Section with gray background, optional text/heading and arbitrary amount of links. Use as link box e.g. with job offers.'



class ProjectTeaserBlock(StructBlock):

    title = CharBlock(required=False, length=256)
    shorttext = RichTextBlock(required=True)
    image = ImageChooserBlock(icon="image")
    internal_link = PageChooserBlock(required=False)
    external_url = URLBlock(required=False, length=256)

    class Meta:
        template = 'blocks/block_project_teaser.html'
        icon = 'placeholder'
        label = 'Project Teaser'
        help_text = 'Use as project teaser, internal link to project page, external link to project URL.'

    
