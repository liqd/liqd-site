from os import path

from django.core.management.commands import makemessages


def get_module_dir(name):
    module = __import__(name)
    return path.dirname(module.__file__)


class Command(makemessages.Command):
    msgmerge_options = (
        makemessages.Command.msgmerge_options + ['--no-fuzzy-matching']
    )

    def handle(self, *args, **options):
        if options['domain'] == 'djangojs':
            if options['extensions'] is None:
                options['extensions'] = ['js', 'jsx']
        return super().handle(*args, **options)

    def find_files(self, root):
        apps_path = super().find_files('apps')
        website_wagtail_paths = super().find_files(
            path.relpath(get_module_dir('website_wagtail')))

        return apps_path + website_wagtail_paths
