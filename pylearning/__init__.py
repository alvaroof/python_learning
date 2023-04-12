# -*- coding: utf-8 -*-
"""Top level package for Python Personal Learning."""
from importlib import metadata
from pathlib import Path


__version__ = metadata.version("pylearning")


# Base path of pylearning module
# (to be used when accessing non .py files in Python Personal Learning/)
BASEPATH = Path(__file__).parent
ASSET_DIR = BASEPATH / "assets"
