from django.utils.html import format_html

from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        """
        <script>
            delete halloPlugins.halloformat;
        </script>
        """
    )
