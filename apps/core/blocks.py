from wagtail.blocks import CharBlock
from wagtail.blocks import ChoiceBlock
from wagtail.blocks import ListBlock
from wagtail.blocks import PageChooserBlock
from wagtail.blocks import RawHTMLBlock
from wagtail.blocks import RichTextBlock
from wagtail.blocks import StructBlock
from wagtail.blocks import URLBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class StandardParagraphBlock(StructBlock):
    headline = CharBlock(required=False, max_length=256)
    text = RichTextBlock(required=True)

    class Meta:
        template = "blocks/block_standard_paragraph.html"
        icon = "pilcrow"
        label = "Basic Paragraph"
        help_text = "Basic text paragraph with optional heading."


class HTMLBlock(StructBlock):
    headline = CharBlock(required=False, max_length=256)
    body = RawHTMLBlock()

    class Meta:
        template = "blocks/block_html.html"
        icon = "code"
        label = "HTML Block"
        help_text = "Unfiltered HTML block with "
        "optional heading. Be sure you know what you do!"


class HighlightParagraphBlock(StructBlock):
    headline = CharBlock(required=False, max_length=256)
    text = RichTextBlock(required=True)
    link = PageChooserBlock(required=False)

    class Meta:
        template = "blocks/block_highlight_paragraph.html"
        icon = "pilcrow"
        label = "Grey Paragraph"
        help_text = "Paragraph with gray background and optional single link."


class QuoteParagraph(StructBlock):
    text = RichTextBlock(required=True)
    color = ChoiceBlock(
        choices=[("green", "Gruen"), ("orange", "Orange"), ("red", "Rot")],
        required=False,
        help_text="Select a color from the list.",
    )
    image = ImageChooserBlock(
        required=False,
        help_text="Please use an image with"
        " at least 800x400px or a similar aspect ratio.",
    )
    author = CharBlock(required=False, max_length=256)

    class Meta:
        template = "blocks/block_quote_paragraph_image.html"
        icon = "pilcrow"
        label = "Quote Paragraph"
        help_text = "Centered text (set quotemarks manually)"
        " with background color or background image and optional author field."


class TeaserBlock(StructBlock):
    headline = CharBlock(required=False, max_length=256)
    text = RichTextBlock(required=True)
    url = URLBlock(required=False)


class TeaserBlockList(StructBlock):
    headline = CharBlock(required=False, max_length=256)
    teasers = ListBlock(TeaserBlock())

    class Meta:
        template = "blocks/teaser_block_list.html"


class ColumnBlock(StructBlock):
    col1_headline = CharBlock(required=False, max_length=256)
    col1_text = RichTextBlock(required=True)
    col1_url = URLBlock(required=False)
    col2_headline = CharBlock(required=False, max_length=256)
    col2_text = RichTextBlock(required=True)
    col2_url = URLBlock(required=False)

    class Meta:
        template = "blocks/block_column.html"
        icon = "grip"
        label = "2 Column Text"
        help_text = "Text in 2 columns with optional column heading."


class ImageSliderBlock(ListBlock):
    ImageChooserBlock(
        label="Image", help_text="Images will be used with a 950x450px size."
    )

    class Meta:
        template = "blocks/block_carousel.html"
        icon = "image"
        label = "Image Slider"
        help_text = "Responsive image slider "
        "(swipe on mobile). Please choose 4 images."


class LinkwithTitleBlock(StructBlock):
    internal_link = PageChooserBlock()
    link_text = CharBlock(max_length=256)


class ImagewithLinkandTitleBlock(StructBlock):
    image = ImageChooserBlock(required=True, label="Image")
    internal_link = PageChooserBlock(required=False)
    external_url = URLBlock(required=False, max_length=256)
    link_text = CharBlock(max_length=256)


class ThreeImageWithLinkBlock(StructBlock):
    image_left = ImagewithLinkandTitleBlock(required=True)
    image_middle = ImagewithLinkandTitleBlock(required=True)
    image_right = ImagewithLinkandTitleBlock(required=True)

    class Meta:
        template = "blocks/three_image_with_link.html"
        icon = "image"
        label = "Three Images"


class LinkboxBlock(StructBlock):
    headline = CharBlock(required=False, max_length=256)
    text = RichTextBlock(required=False)
    links = ListBlock(
        LinkwithTitleBlock(),
    )

    class Meta:
        template = "blocks/block_linkbox.html"
        icon = "link"
        label = "Link Box"
        help_text = "Section with gray background, "
        "optional text/heading and arbitrary amount of links. "
        "Use as link box e.g. with job offers."


class ProjectBlock(StructBlock):
    project = PageChooserBlock(target_model="projects.ProjectPage")


class TeaseredProjectsBlock(StructBlock):
    headline = CharBlock(required=False, max_length=256)
    projects = ListBlock(ProjectBlock)

    class Meta:
        template = "blocks/teasered_projects_block.html"


class AlignedImageBlock(StructBlock):
    image = ImageChooserBlock(label="Image")
    display = ChoiceBlock(
        choices=[("center", "center"), ("left", "left"), ("right", "right")],
        required=True,
        help_text="Decide on which side the image should be displayed",
    )

    class Meta:
        template = "blocks/block_alignedimage.html"


class VideoBlock(StructBlock):
    title = CharBlock(max_length=130, required=False)
    description = CharBlock(
        max_length=500,
        required=False,
        help_text="Please insert a short description of the video "
        "(character limit 500).",
    )
    media = DocumentChooserBlock(
        help_text="Please upload or choose a media "
        "file with any of the following extensions: "
        "MP4, WebM, MP3, WAV"
    )
    media_type = ChoiceBlock(
        choices=[("audio", "Audio file"), ("video", "Video file")]
    )
    transcript = RichTextBlock(
        features=["bold", "italic", "ol", "ul", "link", "document-link"],
        help_text="You can add the video's "
        "transcript here (unlimited "
        "characters).",
        required=False,
    )

    class Meta:
        template = "blocks/block_video.html"
        icon = "media"
        label = "Video Block"
