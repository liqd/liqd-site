VIRTUAL_ENV ?= venv
SOURCE_DIRS = apps website_wagtail contrib
ARGUMENTS=$(filter-out $(firstword $(MAKECMDGOALS)), $(MAKECMDGOALS))

.PHONY: all
all: help

.PHONY: help
help:
	@echo Liquid Website development tools
	@echo
	@echo It will either use an exisiting virtualenv if it was entered
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
	@echo "  make test              -- run Django unit tests"
	@echo "  make test-e2e          -- run Playwright E2E tests (requires server running)"
	@echo "  make test-all          -- run both Django and E2E tests"
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
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements/dev.txt
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

.PHONY: test
test:
	$(VIRTUAL_ENV)/bin/python manage.py test tests/backend

# Internal target to setup E2E test environment
.PHONY: _setup-e2e
_setup-e2e:
	@if [ -f package.json ] && grep -q "@playwright/test" package.json; then \
		if ! ls $$HOME/.cache/ms-playwright/chromium-* 1>/dev/null 2>&1; then \
			echo "Installing Playwright browsers..."; \
			npx playwright install --with-deps chromium || true; \
		fi; \
	fi
	@echo "Creating admin user for E2E tests..."
	@$(VIRTUAL_ENV)/bin/python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@test.com', 'password')" || true

# Internal target to run E2E tests with server
# Usage: $(MAKE) _run-e2e-tests TEST_CMD="npm run test:e2e"
.PHONY: _run-e2e-tests
_run-e2e-tests:
	@echo "Starting Django server on port 8016 for E2E tests..."
	@trap 'kill $$SERVER_PID 2>/dev/null || true' EXIT INT TERM; \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8016 > /tmp/django-server.log 2>&1 & \
	SERVER_PID=$$!; \
	echo "Server started with PID $$SERVER_PID"; \
	sleep 3; \
	$(TEST_CMD); \
	TEST_EXIT=$$?; \
	echo "Stopping server..."; \
	kill $$SERVER_PID 2>/dev/null || true; \
	wait $$SERVER_PID 2>/dev/null || true; \
	exit $$TEST_EXIT

.PHONY: test-e2e
test-e2e: _setup-e2e
	@echo "Running Playwright E2E tests..."
	@$(MAKE) _run-e2e-tests TEST_CMD="TEST_BASE_URL=http://localhost:8016 npm run test:e2e"

.PHONY: test-e2e-ui
test-e2e-ui: _setup-e2e
	@echo "Running Playwright E2E tests with UI..."
	@$(MAKE) _run-e2e-tests TEST_CMD="TEST_BASE_URL=http://localhost:8016 npm run test:e2e:ui"

.PHONY: test-all
test-all: test
	@echo "Django tests completed, starting E2E tests..."
	@$(MAKE) test-e2e
	@echo "All tests completed!"

.PHONY: lint
lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort --diff -c $(SOURCE_DIRS) ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint --silent ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/python manage.py makemigrations --dry-run --check --noinput || EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: lint-quick
lint-quick:
	EXIT_STATUS=0; \
	npm run lint-staged ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/python manage.py makemigrations --dry-run --check --noinput || EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: lint-python-files
lint-python-files:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/black $(ARGUMENTS) || EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/isort --diff -c $(ARGUMENTS) --filter-files || EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(ARGUMENTS) || EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: lint-fix
lint-fix:
	EXIT_STATUS=0; \
	npm run lint-fix ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/isort $(SOURCE_DIRS) --filter-files || EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: po
po:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages --all --extension html,email,py,js,jsx --ignore venv --ignore node_modules

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
