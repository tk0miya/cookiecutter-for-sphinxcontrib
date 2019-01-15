"""
    test_{{ cookiecutter.package_name }}
    ~~~~~{{ '~' * cookiecutter.package_name|length }}

    Test for {{ cookiecutter.package_name }} extension.

    :copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import pytest


@pytest.mark.sphinx('html', testroot='basic')
def test_basic(app, status, warning):
    app.builder.build_all()
