"""
API reference documentation for the example `mytoolbox` package.
"""

from . import mymodule1, mymodule2
from dataclasses import dataclass    # intentionally unused import
from pathlib import Path

HOMEDIR = Path.home()
"""The home directory"""

CONFIG = {1:2, 2:3, 3:4}
"""Some dictionary"""

__version__ = "0.0.1"
"""The version number as dunder attr."""

VERSION = __version__
"""The version number as public attr."""


def version():
    r"""Return version number as func."""
    return __version__


class Version:
    """The version number as class."""
    myattr = 1234
    """some class attribute"""
    __myattr__ = 1234
    """some special class attribute"""
    pathattr = Path.home().joinpath("subdir")
    """some path attribute"""

    @classmethod
    def __repr__(cls):
        return __version__


__all__ = ["__version__", "version", "Version", "VERSION", "CONFIG", "HOMEDIR", "mymodule1", "mymodule2"]
