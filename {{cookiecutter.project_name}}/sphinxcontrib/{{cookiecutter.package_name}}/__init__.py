"""
    sphinxcontrib.{{ cookiecutter.package_name }}
    ~~~~~~~~~~~~~~{{ '~' * (cookiecutter.package_name|length) }}

    :copyright: Copyright 2007-2019 by the Sphinx team, see README.
    :license: BSD, see LICENSE for details.
"""

from typing import Any, Dict
from sphinx.application import Sphinx

from sphinxcontrib.{{ cookiecutter.package_name}}.version import __version__

from sphinx.locale import get_translation

package_dir = path.abspath(path.dirname(__file__))

_ = get_translation(__name__)
__ = get_translation(__name__, 'console')


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_message_catalog(__name__, path.join(package_dir, 'locales'))
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
