# -*- coding: utf-8 -*-
"""Top level package for Novartis Python Training."""
import os
from importlib import metadata
from pathlib import Path

__version__ = metadata.version("python_training")


# Base path of python_training module
# (to be used when accessing non .py files in Novartis Python Training/)
WORKDIR = Path(os.getenv("WORKDIR", Path.cwd()))
BASEPATH = Path(__file__).parent
ASSET_DIR = BASEPATH / "assets"
M3_PATH = BASEPATH / "m3_internal_libraries"
