# Setup

## Install requirements:

* Install and setup `pyenv` following instructions from https://github.com/pyenv/pyenv#installation
  * Run `pyenv install` to install the python version specified in the `.python-version` file
  * Make sure that `pyenv` is working properly by running `which python` and `python --version`
* Install PDM https://pdm.fming.dev/latest/#installation
  * Run `pdm sync` to install all requirements

## Setup for development
* Start a celery worker: `celery -A app.make_celery worker`
* Start redis: `docker compose up -d redis`
* Run your app instance via IDE or `python -m app`
* Head to http://127.0.0.1:3000 to check functionality

## Deployment
* Run `docker compose up -d`
