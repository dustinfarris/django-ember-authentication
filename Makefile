test: lint test-python test-js

lint:
	@echo "Linting Python files"
	flake8 --ignore=E121,W404,F403,E501 --exclude=./docs/*,./env/*,./venv/*,migrations,.git,./tests/functional/features,./tests/functional/steps . || exit 1
	@echo ""

test-python:
	@echo "Running Python tests"
	python manage.py test --settings=server.test_settings || exit 1
	@echo ""

test-js:
	@echo "Running QUnit Javascript tests"
	node_modules/.bin/karma start --reporters=dots || exit 1
	@echo ""

develop:
	npm install
	pip install --upgrade setuptools
	pip install --upgrade "flake8>=2.0"
	pip install --upgrade -r requirements.txt
	python manage.py syncdb --noinput

run:
	python manage.py runserver 0.0.0.0:8000
