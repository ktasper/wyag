"""
Handlers for the version command
"""

import sys
import tomllib
from argparse import Namespace


def cmd_version(args: Namespace) -> None:
    """
    Prints the version of this tool out to STDOUT
    """
    print(get_version(args), file=sys.stdout)


def get_version(args: Namespace) -> str:
    """
    Reads the '.pyproject.toml' file and returns the version of the tool
    """
    with open("./pyproject.toml", "rb") as f:  # Open in binary mode
        data = tomllib.load(f)
        return data["tool"]["poetry"]["version"]
