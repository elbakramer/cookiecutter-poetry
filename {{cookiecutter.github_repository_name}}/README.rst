{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}
{%- if is_open_source %}

.. container::

    .. image:: https://img.shields.io/pypi/v/{{ cookiecutter.python_package_name }}.svg
            :target: https://pypi.python.org/pypi/{{ cookiecutter.python_package_name }}
            :alt: PyPI Version

    .. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.python_package_name }}.svg
            :target: https://pypi.python.org/pypi/{{ cookiecutter.python_package_name }}/
            :alt: PyPI Python Versions

    .. image:: https://img.shields.io/pypi/status/{{ cookiecutter.python_package_name }}.svg
            :target: https://pypi.python.org/pypi/{{ cookiecutter.python_package_name }}/
            :alt: PyPI Status

    .. badges from below are commendted out

    .. .. image:: https://img.shields.io/pypi/dm/{{ cookiecutter.python_package_name }}.svg
            :target: https://pypi.python.org/pypi/{{ cookiecutter.python_package_name }}/
            :alt: PyPI Monthly Donwloads

.. container::

    .. image:: https://img.shields.io/github/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/CI/master
            :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/actions/workflows/ci.yml
            :alt: CI Build Status
    .. .. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/actions/workflows/ci.yml/badge.svg?branch=master

    .. image:: https://img.shields.io/github/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/Documentation/master?label=docs
            :target: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.github_repository_name }}/
            :alt: Documentation Build Status
    .. .. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/actions/workflows/documentation.yml/badge.svg?branch=master

    .. image:: https://img.shields.io/codecov/c/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg
            :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}
            :alt: Codecov Coverage
    .. .. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/branch/master/graph/badge.svg

    .. image:: https://img.shields.io/requires/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/master.svg
            :target: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/requirements/?branch=master
            :alt: Requires.io Requirements Status
    .. .. image:: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/requirements.svg?branch=master

    .. badges from below are commendted out

    .. .. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg
            :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}
            :alt: Travis CI Build Status
    .. .. image:: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg?branch=master

    .. .. image:: https://img.shields.io/readthedocs/{{ cookiecutter.github_repository_name }}/latest.svg
            :target: https://{{ cookiecutter.python_package_name | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
            :alt: ReadTheDocs Documentation Build Status
    .. .. image:: https://readthedocs.org/projects/{{ cookiecutter.github_repository_name }}/badge/?version=latest

    .. .. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/shield.svg
            :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/
            :alt: PyUp Updates

.. container::

    .. image:: https://img.shields.io/pypi/l/{{ cookiecutter.python_package_name }}.svg
            :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/blob/master/LICENSE
            :alt: PyPI License

    .. image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2F{{ cookiecutter.github_username }}%2F{{ cookiecutter.github_repository_name }}.svg?type=shield
            :target: https://app.fossa.com/projects/git%2Bgithub.com%2F{{ cookiecutter.github_username }}%2F{{ cookiecutter.github_repository_name }}?ref=badge_shield
            :alt: FOSSA Status

.. container::

    .. image:: https://badges.gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg
            :target: https://gitter.im/{{ cookiecutter.github_repository_name }}/community
            :alt: Gitter Chat
    .. .. image:: https://img.shields.io/gitter/room/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg

    .. image:: https://img.shields.io/badge/code%20style-black-000000.svg
            :target: https://github.com/psf/black
            :alt: Code Style: Black
{%- endif %}

{{ cookiecutter.project_description }}
{%- if is_open_source %}

* Free software: `{{ cookiecutter.open_source_license }}`_
* Documentation: https://{{ cookiecutter.python_package_name | replace("_", "-") }}.readthedocs.io.
{%- endif %}

.. _`{{ cookiecutter.open_source_license }}`: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/blob/master/LICENSE

Features
--------

* TODO

Install
-------

.. code-block:: console

    # Install pipx if poetry is not installed
    $ python -m pip install pipx
    $ python -m pipx ensurepath

    # Install poetry using pipx
    $ pipx install poetry

    # Install dependencies
    $ poetry install

Credits
-------

This package was created with Cookiecutter_ and the `elbakramer/cookiecutter-poetry`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elbakramer/cookiecutter-poetry`: https://github.com/elbakramer/cookiecutter-poetry
