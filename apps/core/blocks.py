from wagtail.wagtailcore.blocks import (CharBlock, ChoiceBlock, ListBlock,
                                        PageChooserBlock, RawHTMLBlock,
                                        RichTextBlock, StructBlock, URLBlock)
from wagtail.wagtailimages.blocks import ImageChooserBlock


class StandardParagraphBlock(StructBlock):

    headline = CharBlock(required=False, length=256)
    text = RichTextBlock(required=True)

    class Meta:
        template = 'blocks/block_standard_paragraph.html'
        icon = 'pilcrow'
        label = 'Basic Paragraph'
        help_text = 'Basic text paragraph with optional heading.'


class HTMLBlock(StructBlock):
    headline = CharBlock(required=False, length=256)
    body = RawHTMLBlock()

    class Meta:
        template = 'blocks/block_html.html'
        icon = 'code'
        label = 'HTML Block'
        help_text = 'Unfiltered HTML block with '
        'optional heading. Be sure you know what you do!'


class HighlightParagraphBlock(StructBlock):

    headline = CharBlock(required=False, length=256)
    text = RichTextBlock(required=True)
    link = PageChooserBlock(required=False)

    class Meta:
        template = 'blocks/block_highlight_paragraph.html'
        icon = 'pilcrow'
        label = 'Grey Paragraph'
        help_text = 'Paragraph with gray background and optional single link.'


class QuoteParagraph(StructBlock):

    text = RichTextBlock(required=True)
    color = ChoiceBlock(
        choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')],
        required=False,
        help_text='Select a color from the list.'
    )
    image = ImageChooserBlock(
        required=False,
        help_text='Please use an image with'
        ' at least 800x400px or a similar aspect ratio.'
    )
    author = CharBlock(required=False, length=256)

    class Meta:
        template = 'blocks/block_quote_paragraph_image.html'
        icon = 'pilcrow'
        label = 'Quote Paragraph'
        help_text = 'Centered text (set quotemarks manually)'
        ' with background color or background image and optional author field.'


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
        label='Image',
        help_text='Images will be used with a 950x450px size.'
    )

    class Meta:
        template = 'blocks/block_carousel.html'
        icon = 'image'
        label = 'Image Slider'
        help_text = 'Responsive image slider '
        '(weipe on mobile). Please choose 4 images.'


class LinkwithTitleBlock(StructBlock):
    internal_link = PageChooserBlock()
    link_text = CharBlock(length=256)


class ImagewithLinkandTitleBlock(StructBlock):
    image = ImageChooserBlock(required=True, label='Image')
    internal_link = PageChooserBlock(required=False)
    external_url = URLBlock(required=False, length=256)
    link_text = CharBlock(length=256)


class ThreeImageWithLinkBlock(StructBlock):
    image_left = ImagewithLinkandTitleBlock(required=True)
    image_middle = ImagewithLinkandTitleBlock(required=True)
    image_right = ImagewithLinkandTitleBlock(required=True)

    class Meta:
        template = 'blocks/three_image_with_link.html'
        icon = 'image'
        label = 'Three Images'


class LinkboxBlock(StructBlock):
    headline = CharBlock(required=False, length=256)
    text = RichTextBlock(required=False)
    links = ListBlock(
        LinkwithTitleBlock(),
    )

    class Meta:
        template = 'blocks/block_linkbox.html'
        icon = 'link'
        label = 'Link Box'
        help_text = 'Section with gray background, '
        'optional text/heading and arbitrary amount of links. '
        'Use as link box e.g. with job offers.'


class ProjectBlock(StructBlock):
    project = PageChooserBlock(target_model='projects.ProjectPage')


class TeaseredProjectsBlock(StructBlock):
    headline = CharBlock(required=False, length=256)
    projects = ListBlock(ProjectBlock)

    class Meta:
        template = 'blocks/teasered_projects_block.html'


class AlignedImageBlock(StructBlock):
    image = ImageChooserBlock(label='Image')
    display = ChoiceBlock(
        choices=[('left', 'left'), ('right', 'right')],
        required=True,
        help_text='Decide on which side the image should be displayed'
    )
