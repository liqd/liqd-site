import bleach
from bleach.css_sanitizer import CSSSanitizer
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe


def clean_html_all(text: str) -> SafeString:
    css_sanitizer = CSSSanitizer(allowed_css_properties=[])
    return mark_safe(
        bleach.clean(
            text,
            tags={},
            attributes={},
            css_sanitizer=css_sanitizer,
            strip=True,
        )
    )
