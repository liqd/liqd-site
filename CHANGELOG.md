# Changelog

All notable changes to this project will be documented in this file.

Since version v2407.1 the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
This project (not yet) adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v2407.1

### Added

- add a CHANGELOG.md and changelog/ folder
- add pyproject.toml
- add black for autoformatting
- added matomo integration
- add django-debug-toolbar and enable for development
- add templatetag 'clean_html_all' which strips all css and html tags using
  Bleach

### Changed

- update and pin liquid-logo to v2407.1
- add requirements folder to allow more fine grained dependencies
- move isort config to pyproject.toml
- moved academy page date from the list tile to the detail page (#374)
- Django from 3.2.18 to 4.0
  - remove app label from `__init__.py` inside academy app
  - replace `re_path` with `path` for included urls.
  - remove `USE_L10N` in settings as it is now True by default
  - replace `postgresql_psycopg2` with `postgresql` in ci settings
  - replace blocktransl with blocktranslate
- Django from 4.0 to 4.2
  - settings STATICFILES_STORAGE to STORAGES
  - add the update_fields keyword argument in customised model's save() methods
`_home-logo-scss` fix issues with logo container z-index- update wagtail to 4.2x
- fix deprecated wagtail imports
- update wagtail to 5.0.2
- adjust to new slug field behavior in wagtail 5.0.x
- update wagtail to 5.1.3
- update to wagtail 5.2.5
- use new clean_html_all templatetag to replace django-bleach
- update Bleach to 6.x
- apps/core: use inset shorthand to satisfy linter
- update stylelint to 16.x and styleint-scss to 13.x

### Removed

- Event option from the topic items in academy
- Headline from basic text paragraph
- removed the custom django-compressor classes in contrib/sass as we don't use
  django-compressor anymore
- removed outdated django-bleach dependency
- remove unneded eslint-plugin-n

### Fixed

- fixed contrast checker trying to read potentially empty array

