# -*- coding: utf-8 -*-
"""Example test file (consider removing it)."""
from pylearning.utils import say_hello_to
from pylearning import __version__
import importlib.metadata as im


def test_hello_world(mike):
    """Dummy test function."""
    assert say_hello_to(mike) == "hello Mike"


def test_version_compatibility():
    """Test that versions in __init__ and in pyproject.toml are the same"""
    assert im.version("pylearning") == __version__
