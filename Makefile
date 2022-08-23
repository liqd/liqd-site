VIRTUAL_ENV ?= venv
SOURCE_DIRS = apps website_wagtail
ARGUMENTS=$(filter-out $(firstword $(MAKECMDGOALS)), $(MAKECMDGOALS))

.PHONY: all
all: help

.PHONY: help
help:
	@echo Liquid Website development tools
	@echo
	@echo It will either use am exisiting virtualenv if it was entered
	@echo before or create a new one in the same directory.
	@echo
	@echo usage:
	@echo
	@echo "  make install           -- install dev setup"
	@echo "  make clean             -- delete node modules and venv"
	@echo "  make watch             -- start a dev server and rebuild js and css files on changes"
	@echo "  make server            -- development server"
	@echo "  make lighthouse        -- run lighthouse test on stage server"
	@echo "  make lighthouse-local  -- run lighthouse test on local (requires the server to be running/make watch)"
	@echo "  make lint              -- lint javascript and python"
	@echo "  make lint-fix          -- fix linting for all js files staged in git"
	@echo "  make release           -- build everything required for a release"
	@echo "  make po                -- create new po files from the source"
	@echo "  make mo                -- create new mo files from the translated po files"
	@echo


.PHONY: install
install:
	npm install
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

.PHONY: clean
clean:
	if [ -f package-lock.json ]; then rm package-lock.json; fi
	if [ -d node_modules ]; then rm -rf node_modules; fi
	if [ -d venv ]; then rm -rf venv; fi

.PHONY: watch
watch:
	trap 'kill %1' KILL; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8006

.PHONY: server
server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8006

.PHONY: lighthouse
lighthouse:
	npm run lighthouse

.PHONY: lighthouse-local
lighthouse-local:
	npm run lighthouse-local

.PHONY: lint
lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort --diff -c $(SOURCE_DIRS) ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint --silent ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/python manage.py makemigrations --dry-run --check --noinput || EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: lint-fix
lint-fix:
	EXIT_STATUS=0; \
	npm run lint-fix ||  EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: po
po:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages --all --extension html,email,py,js,jsx --ignore venv --ignore node_modules
	msgen locale/de/LC_MESSAGES/django.po -o locale/de/LC_MESSAGES/django.po

.PHONY: mo
mo:
	$(VIRTUAL_ENV)/bin/python manage.py compilemessages

.PHONY: release
release: export DJANGO_SETTINGS_MODULE ?= website_wagtail.settings.build
release:
	npm install --silent
	npm run build:prod
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements.txt -q
	$(VIRTUAL_ENV)/bin/python3 manage.py compilemessages -v0
	$(VIRTUAL_ENV)/bin/python3 manage.py collectstatic --noinput -v0
