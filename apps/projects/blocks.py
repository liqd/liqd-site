from wagtail.wagtailcore import blocks


class FactBlock(blocks.StructBlock):
    label = blocks.CharBlock()
    fact = blocks.RichTextBlock()


class FactListBlock(blocks.StructBlock):
    facts = blocks.ListBlock(FactBlock)

    class Meta:
        template = 'blocks/fact_list_block.html'
