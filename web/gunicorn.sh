#!/bin/bash
NAME='bookmarks_gunicorn'
PROJECT_PATH="/home/`whoami`/web/bookmarks"
VIRTUALENV_PATH="/home/`whoami`/web/bookmarks/venv"
ADDRESS="0.0.0.0:5000"
WORKERS=2
DJANGO_SETTINGS_MODULE="bookmarks.settings.production"

echo "Starting $NAME as `whoami`"

source $VIRTUALENV_PATH/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

cd $PROJECT_PATH

echo $PROJECT_PATH

exec gunicorn bookmarks.wsgi:application --bind=$ADDRESS --workers=$WORKERS --pid /tmp/gunicorn.pid --daemon
