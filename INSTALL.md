# Setup

## Installing requirements (recommended):

* Install and setup `pyenv` following instructions from https://github.com/pyenv/pyenv#installation
  * Run `pyenv install` to install the python version specified in the `.python-version` file
  * Make sure that `pyenv` is working properly by running `which python` and `python --version`
* Install PDM https://pdm.fming.dev/latest/#installation
  * Run `pdm sync` to install all requirements

## Installing requirements (conda):
* Install conda (you know what to do)
* Install the python version specified in the `.python-version` file
* Run `conda install pip` to install `pip`
* Run `pip install -r requirements.txt` to install all requirements

## Manage requirements
* Please refer to the official pdm documentation at https://pdm.fming.dev/latest/usage/dependency
* Make sure to run `pdm export -o requirements.txt --without-hashes` to keep the `requirements.txt` file up to date
* 