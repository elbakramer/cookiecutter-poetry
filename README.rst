===================
Cookiecutter Poetry
===================

Cookiecutter_ template for a Python package using Poetry_.

.. image:: https://github.com/elbakramer/cookiecutter-poetry/workflows/Python%20test/badge.svg?branch=master
    :target: https://github.com/elbakramer/cookiecutter-poetry/actions
    :alt: Linux build status on Github Actions

* GitHub repo: https://github.com/elbakramer/cookiecutter-poetry/
* Documentation: https://elbakramer.github.io/cookiecutter-poetry/
* Free software: MIT License

Features
--------

* Package and dependency management using Poetry_

  * Has option to stick with setuptools (setup.py)

* `Github Actions`_: Ready for GitHub Actions

  * Build and test on push or pull request for continuous integration (CI) (+badge)
  * Build documentation on push, publish the built documentation to Github Pages (+badge)
  * Draft release on push, this draft can be published manually or even automatically when new tag is pushed
  * Build and release Python package to PyPI_ when new release tag is published on github

* Many `pre-commit`_ hook based formatting, linting, testing tools

  * Upgrade syntax for newer python with pyupgrade_
  * Formatting with black_
  * Import sorting with isort_
  * Linting with flake8_ and pylint_
  * Static typing with mypy_
  * Testing with pytest_
  * Git hooks that run all the above with `pre-commit`_

* Other integrations to external sites/services

  * Sphinx_ docs serving with ReadTheDocs_ (+badge)
  * Coverage report with Codecov_ (+badge)
  * Monitoring depedency version updates with `Requires.io`_ or PyUp_ (+badge)

* Version bumping using bump2version_
* Dynamic versioning using dunamai_
* Command line interface using Click_

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet
(this requires Cookiecutter 1.4.0 or higher)::

    # Install pipx
    $ pip install pipx
    $ pipx ensurepath

    # Install cookiecutter using pipx
    $ pipx install cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/elbakramer/cookiecutter-poetry.git

Then, if you choose to try poetry::

    # Install pipx
    $ pip install pipx
    $ pipx ensurepath

    # Install poetry using pipx
    $ pipx install poetry

    # Run `poetry install` to install dependencies
    $ cd {{ cookiecutter.github_repository_name }}/
    $ poetry install

    # Initialize git
    $ git init

    # Install pre-commit hooks
    $ poetry run pre-commit install

    # Do initial commit
    $ git add --all
    $ git commit -m "Initial commit"

Or, if you choose to stick with setuptools::

    # Install dependencies using pip
    $ cd {{ cookiecutter.github_repository_name }}/
    $ pip install --editable .[dev]

    # Initialize git
    $ git init

    # Install pre-commit hooks
    $ pre-commit install

    # Do initial commit
    $ git add --all
    $ git commit -m "Initial commit"

Lastly, you can:

* Create a github repo and push there.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `johanvergeer/cookiecutter-poetry`_: Direct ancestor of this package, using ``poetry`` as package manager.
* `sourcery-ai/python-best-practices-cookiecutter`_: Features many useful development tools with ``pre-commit`` hooks, took as reference during development.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

.. _`johanvergeer/cookiecutter-poetry`: https://github.com/johanvergeer/cookiecutter-poetry
.. _`sourcery-ai/python-best-practices-cookiecutter`: https://github.com/sourcery-ai/python-best-practices-cookiecutter

.. _`network`: https://github.com/elbakramer/cookiecutter-poetry/network
.. _`family tree`: https://github.com/elbakramer/cookiecutter-poetry/network/members

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Poetry: https://python-poetry.org/
.. _Github Actions: https://github.com/features/actions
.. _PyPi: https://pypi.org/
.. _`pre-commit`: https://pre-commit.com/
.. _pyupgrade: https://github.com/asottile/pyupgrade
.. _black: https://github.com/psf/black
.. _isort: https://github.com/PyCQA/isort
.. _flake8: https://github.com/PyCQA/flake8
.. _pylint: https://github.com/PyCQA/pylint/
.. _mypy: https://github.com/python/mypy
.. _pytest: https://docs.pytest.org/en/stable/contents.html
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _Codecov: https://about.codecov.io/
.. _`Requires.io`: https://requires.io/
.. _PyUp: https://pyup.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _dunamai: https://github.com/mtkennerly/dunamai
.. _Click: https://click.palletsprojects.com/en/7.x/
