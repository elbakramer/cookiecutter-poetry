============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `{{ cookiecutter.github_repository_name }}` for local development.

1. Fork the `{{ cookiecutter.github_repository_name }}` repo on GitHub.

2. Clone your fork locally:

   .. code-block:: console

       $ git clone https://github.com/your_name_here/{{ cookiecutter.github_repository_name }}.git

3. Set up your fork for local development:

   .. code-block:: console
{%- if cookiecutter.use_poetry == "y" %}

       $ # Install poetry if you don't have one:
       $ # https://python-poetry.org/docs/#installation

       $ # Example below will install poetry using pipx

       $ # Install ``pipx``
       $ pip install pipx
       $ pipx ensurepath

       $ # Install ``poetry`` using ``pipx``
       $ pipx install poetry

       $ # Run ``poetry install`` to install dependencies
       $ cd {{ cookiecutter.github_repository_name }}/
       $ poetry install
{%- else %}

       $ # Install dependencies using ``pip``
       $ cd {{ cookiecutter.github_repository_name }}/
       $ pip install --editable .[dev]
{%- endif %}

       $ # Install ``pre-commit`` hooks
       $ {% if cookiecutter.use_poetry == "y" %}poetry run {% endif %}pre-commit install
{%- if cookiecutter.use_poetry == "y" %}

   When you run ``poetry install``, all the dependencies including development tools will be installed under a virtualenv managed by poetry.

   Then you can run those commands using ``poetry run command args...``, like the last command in the example above.
{%- endif %}

4. Create a branch for local development:

   .. code-block:: console

       $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, you can check if your changes pass some checks:

   .. code-block:: console

       $ # Code formatters
       $ {% if cookiecutter.use_poetry == "y" %}poetry run {% endif %}isort .
       $ {% if cookiecutter.use_poetry == "y" %}poetry run {% endif %}black .

       $ # Linters and Static analysis tools
       $ {% if cookiecutter.use_poetry == "y" %}poetry run {% endif %}flake8 {{ cookiecutter.python_package_name }} tests
       $ {% if cookiecutter.use_poetry == "y" %}poetry run {% endif %}pylint {{ cookiecutter.python_package_name }} tests
       $ {% if cookiecutter.use_poetry == "y" %}poetry run {% endif %}mypy {{ cookiecutter.python_package_name }} tests

       $ # Testing
       $ {% if cookiecutter.use_poetry == "y" %}poetry run {% endif %}pytest --cov

   Or you can just commit/push your changes to make pre-commit hooks trigger those checks automatically.
   If you want to skip those hooks temporarily, add `--no-verify` option for git commit/push.

6. Commit your changes and push your branch to GitHub:

   .. code-block:: console

       $ git add .
       $ git commit -m "Your detailed description of your changes."
       $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.8 and 3.9. Check
   https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/actions/workflows/ci.yml
   and make sure that the tests pass for all supported Python versions.

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run:

.. code-block:: console

    $ {% if cookiecutter.use_poetry == "y" %}poetry run {% endif %}bump2version patch  # possible: major / minor / patch
    $ git push
    $ git push --follow-tags

Travis will then deploy to PyPI if tests pass.
