from wagtail.blocks import (CharBlock, ListBlock, PageChooserBlock,
                            RichTextBlock, StructBlock, TextBlock, URLBlock)
from wagtail.images.blocks import ImageChooserBlock


class ChallengeStepBlock(StructBlock):
    challenge_step_title = CharBlock()
    challenge_step_text = RichTextBlock(required=False)
    links = ListBlock(StructBlock(
        [
            ("challenge_step_academy_links", PageChooserBlock(
                target_model='academy.AcademyPage',
                required=False,
                help_text='Add an academy link OR a non academy link, NOT BOTH!'
            )),
            ("challenge_step_external_links", PageChooserBlock(
                target_model='academy.AcademyExternalLink',
                required=False))
        ]
    )
    )

    class Meta:
        template = 'academy/blocks/block_academy_challenge.html'
        icon = 'grip'
        label = 'Academy challenge step'
        help_text = 'Select the pages to be included in this challenge step'


# sublock for internal and external links
class LinkBlock(StructBlock):
    internal_link = PageChooserBlock(
        required=False,
        label="Internal Link",
        help_text="The external link overwrites the link to a local page. Please only add 1 link."
    )
    external_link = URLBlock(
        required=False,
        label="External Link",
    )


class AcademySingleTeaserBlock(StructBlock):
    category = CharBlock(required=False, length=32)
    headline = CharBlock(required=True, length=74)
    body_text = TextBlock(required=True, length=164)
    link = StructBlock([
        ('internal_link', PageChooserBlock(required=False)),
        ('external_link', URLBlock(required=False)),
    ],
    help_text="The external link overwrites the link to a local page. Please only add 1 link."
    )
    link_text = CharBlock(required=True, length=24)
    image = ImageChooserBlock(required=True)

    class Meta:
        template = 'academy/blocks/single_teaser_block.html'
        icon = 'image'
        label = 'Single teaser block'
