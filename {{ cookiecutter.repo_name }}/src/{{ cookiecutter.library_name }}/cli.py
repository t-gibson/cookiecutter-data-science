"""
CLI to execute different analysis steps.
"""

import click

from {{ cookiecutter.library_name }}.version import __version__


@click.group()
@click.version_option(version=__version__)
def main():
    pass
