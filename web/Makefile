.SILENT:

PYTHON=$(shell which python)
PIP=venv/bin/pip
PY_TEST=venv/bin/py.test
GUNICORN=venv/bin/gunicorn

debug: clean
	${PYTHON} manage.py runserver 0.0.0.0:5001 --settings=bookmarks.settings.base

clean:
	find . \( -name *.py[co] -o -name __pycache__ \) -delete

venv:
	virtualenv venv

setup: venv
	${PIP} install -U pip
	${PIP} install -r requirements.txt

setup-local: venv
	${PIP} install -U pip
	${PIP} install -r requirements.txt
	${PIP} install -r requirements_dev.txt

test: clean
	${PY_TEST} -s -r a --color=yes

test-cov: clean
	${PY_TEST} --cov=menu --cov-report=term --cov-report=html -s -r a --color=yes

collectstatic:
	${PYTHON} manage.py collectstatic --noinput --settings=bookmarks.settings.production

gunicorn:
	gunicorn bookmarks.wsgi:application --bind=0.0.0.0:5001
