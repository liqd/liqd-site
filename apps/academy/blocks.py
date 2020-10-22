from wagtail.core.blocks import (CharBlock, ListBlock, StructBlock,
                                RichTextBlock, PageChooserBlock)

class ChallengeLinkBlock(StructBlock):
    challenge_step_academy_links = PageChooserBlock(
        target_model='academy.AcademyPage',
        required=False,
        help_text='Add an academy page')

class ChallengeExternalLinkBlock(StructBlock):
    challenge_step_external_links = PageChooserBlock(
        target_model='academy.AcademyExternalLink',
        required=False,
        help_text='Add a non academy page')


class ChallengeStepBlock(StructBlock):
    challenge_step_title = CharBlock()
    challenge_step_text = RichTextBlock(required=False)
    links = ListBlock(StructBlock(
        [
            ("challenge_step_academy_links", PageChooserBlock(
                target_model='academy.AcademyPage',
                required=False,)),
            ("challenge_step_external_links", PageChooserBlock(
                target_model='academy.AcademyExternalLink',
                required=False,))
        ]
    )
    )

    class Meta:
        template = 'academy/blocks/block_academy_challenge.html'
        icon = 'grip'
        label = 'Academy challenge step'
        help_text = 'Select the pages to be included in this challenge step'
