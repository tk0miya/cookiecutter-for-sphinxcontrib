"""
    sphinxcontrib.{{ cookiecutter.package_name }}
    ~~~~~~~~~~~~~~{{ '~' * (cookiecutter.package_name|length) }}

    :copyright: Copyright 2007-2019 by the Sphinx team, see README.
    :license: BSD, see LICENSE for details.
"""

from typing import Any, Dict
from sphinx.application import Sphinx

from sphinxcontrib.{{ cookiecutter.package_name}}.version import __version__


def setup(app: Sphinx) -> Dict[str, Any]:
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
