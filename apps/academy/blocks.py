from django.template.defaulttags import register
from wagtail.blocks import (CharBlock, ChoiceBlock, ListBlock,
                            PageChooserBlock, RichTextBlock, StructBlock,
                            TextBlock, URLBlock)
from wagtail.images.blocks import ImageChooserBlock

from apps.academy.choices import TOPIC_CHOICES


class ChallengeStepBlock(StructBlock):
    challenge_step_title = CharBlock()
    challenge_step_text = RichTextBlock(required=False)
    links = ListBlock(StructBlock(
        [
            ("challenge_step_academy_links", PageChooserBlock(
                target_model='academy.AcademyPage',
                required=False,
                help_text='Add link to a challenge page either internal '
                'or external'
                )),
            ("challenge_step_external_links", PageChooserBlock(
                target_model='academy.AcademyExternalLink',
                required=False, ))
        ]
    ))

    class Meta:
        template = 'academy/blocks/block_academy_challenge.html'
        icon = 'grip'
        label = 'Academy challenge step'
        help_text = 'Select the pages to be included in this challenge step'


class AcademySingleTeaserBlock(StructBlock):
    category = CharBlock(required=False, max_length=32)
    headline = CharBlock(required=True, max_length=74)
    body_text = TextBlock(required=True, max_length=164)
    link = PageChooserBlock(
        required=False,
        help_text="Please only add either an internal or external link")
    external_link = URLBlock(
        required=False,
        label="External Link",
        help_text="The external link overwrites the link to a local page."
    )
    link_text = CharBlock(required=True, max_length=24)
    image = ImageChooserBlock(required=True)

    class Meta:
        template = 'academy/blocks/single_teaser_block.html'
        icon = 'image'
        label = 'Single teaser block'


# sub block for AcademyCallToActionBlock
class CallToActionBlock(StructBlock):
    headline = CharBlock(required=True, max_length=28)
    image = ImageChooserBlock(
        required=True,
        help_text="Please add image with transparent background")
    body_text = TextBlock(required=True, max_length=120)
    cta_link = StructBlock([
        ('internal_link', PageChooserBlock(required=False,
                                           help_text="The external link "
                                           "overwrites the link to a local "
                                           "page. Please only add 1 link.")),
        ('external_link', URLBlock(required=False)),
    ])
    link_text = CharBlock(
        required=False, max_length=28, label='Link Text'
    )
    anchor_link = CharBlock(
        required=False, max_length=28, label='Anchor Link',
        help_text="Anchor link should be all one word."
    )


class AcademyCallToActionBlock(StructBlock):
    columns = ListBlock(
        CallToActionBlock(label='List and Image'),
        max_num=2
    )

    class Meta:
        template = 'academy/blocks/block_col_cta.html'
        icon = 'plus-inverse'
        help_text = 'Add 1 or 2 column teaser with black '
        'background and white writing'


class TopicBlock(StructBlock):
    topic_category = ChoiceBlock(
        choices=TOPIC_CHOICES,
        required=True,
        help_text='Select a topic'
    )
    topic_text = CharBlock(required=True, max_length=110)
    topic_link_text = CharBlock(required=True, max_length=40)


class TopicBlockList(StructBlock):
    title = CharBlock(required=True, max_length=74)
    topics = ListBlock(TopicBlock(), min_num=3, max_num=3)
    topic_url = PageChooserBlock(
        required=True,
        page_type='academy.AcademyIndexPage'
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['topics_dict'] = dict(TOPIC_CHOICES)
        return context

    class Meta:
        template = 'academy/blocks/block_topic_teaser.html'
        icon = 'grip'
        label = '3 topic teasers'


@register.filter
def get_category_name(dict, key):
    return dict.get(key)
