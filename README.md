# Flet_Material3_Demo
Rebuilding the [Flutter version](https://flutter.github.io/samples/web/material_3_demo/#/) using the [Flet](https://flet.dev) python framework.

## Getting Started (Pyenv + Poetry)
* Install [pyenv-win](https://github.com/pyenv-win/pyenv-win)(for windows) or [pyenv](https://github.com/pyenv/pyenv)(for linux)
* Install [Poetry](https://python-poetry.org/docs/#installation)
* Set python version: 
```commandline
pyenv install --skip-existing && pyenv local
```
* Install project requirements:
```commandline
poetry install
```
* If env not active:
```commandline
poetry shell
```

## Getting Started (Pip)
* Install [Python 3.11.0](https://www.python.org/downloads/)
* Set up virtual environment:
```commandline
python -m venv /venv
```
* Activate virtual environment:
```commandline
/venv/Scripts/activate
```
* Install project requirements:
```commandline
pip install -r requirements.txt
```

* Run app with hot-reload: <br>
```commandline
flet run main.py -r
```
Reload triggers on main app file and sub folders changes as long as -r (--recursive) active.<br>! Reload does not save state of the app at the moment this readme was written.
