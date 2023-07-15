# Flet Material3 Demo
Rebuilding the Flutter version([web link](https://flutter.github.io/samples/web/material_3_demo/#/), [GitHub repo](https://github.com/chayanforyou/flutter_material_3_demo/blob/master/lib/main.dart)) using the [Flet](https://flet.dev) python framework.

## Getting Started 
* Install [Python](https://www.python.org/downloads/)
* Set up and activate a virtual environment:
* Install project requirements:
```commandline
pip install -r requirements.txt
```
* Clone this project creating your local version, move into the folder, then run the app: 
  - normally:
    ```commandline
    python main.py
    ```
  - with hot-reload:
    ```commandline
    flet run main.py -r
    ```
    Reload triggers on main app file and sub folders changes as long as `-r` (`--recursive`) active. Reload does not save state of the app at time of writing.
