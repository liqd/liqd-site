from django.utils import translation
from wagtail.blocks.stream_block import StreamValue
from wagtail.core.blocks import StructValue


class TranslatedField(object):

    def __init__(self, de_field, en_field):
        self.de_field = de_field
        self.en_field = en_field

    def hasContent(self, field):
        if isinstance(field, StreamValue):
            value = field.raw_data
            if value:
                return True
            else:
                return False
        elif isinstance(field, str):
            if field:
                return True
            else:
                return False
        else:
            return False

    def __get__(self, instance, owner):
        de = getattr(instance, self.de_field)
        en = getattr(instance, self.en_field)

        if translation.get_language() == 'en' and self.hasContent(en):
            return en
        elif self.hasContent(de):
            return de
        return en


class TranslatedStructValue(StructValue):

    def translated_link_text(self):
        if translation.get_language() == 'en' and self.get('link_text_en'):
            return self.get('link_text_en')
        elif self.get('link_text_de'):
            return self.get('link_text_de')
        return self.get('link_text_en')
