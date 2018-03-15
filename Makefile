all: help

VIRTUAL_ENV ?= venv
SOURCE_DIRS = apps website_wagtail

help:
	@echo Liquid Website development tools
	@echo
	@echo It will either use am exisiting virtualenv if it was entered
	@echo before or create a new one in the same directory.
	@echo
	@echo usage:
	@echo
	@echo   make install  -- install dev setup
	@echo   make server	  -- development server
	@echo   make test     -- tests on exiting database
	@echo   make lint	    -- lint javascript and python
	@echo   make release  -- build everything required for a release
	@echo


install:
	npm install
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

watch:
	trap 'kill %1' KILL; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8006

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8006

lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort -rc -c $(SOURCE_DIRS) ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint --silent ||  EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: release
release: export DJANGO_SETTINGS_MODULE ?= website_wagtail.settings.build
release:
	npm install --silent
	npm run build
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements.txt -q
	$(VIRTUAL_ENV)/bin/python3 manage.py compilemessages -v0
	$(VIRTUAL_ENV)/bin/python3 manage.py collectstatic --noinput -v0
