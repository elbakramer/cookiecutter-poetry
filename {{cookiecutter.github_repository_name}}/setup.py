#!/usr/bin/env python

"""The setup script."""

from __future__ import annotations

from setuptools import find_packages, setup

with open("README.rst", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst", encoding="utf-8") as history_file:
    history = history_file.read()

requirements: list[str] = []

requirements_dev = [
    "actions-toolkit>=0.0.5",
    "black>=21.5b0",
    "bump2version>=1.0.1",
    "codecov>=2.1.11",
    "coverage>=5.5",
    "dunamai>=1.5.5",
    "flake8>=3.9.1",
    "isort>=5.8.0",
    "mypy>=0.812",
    "pip-tools>=6.1.0",
    "pre-commit>=2.12.1",
    "pylint>=2.8.2",
    "pytest>=6.2.4",
    "pytest-cov>=2.11.1",
    "pytest-xdist>=2.2.1",
]

requirements_docs = [
    "Sphinx>=3.5.4",
    "sphinx-autoapi>=1.8.1",
]

requirements_dev += requirements_docs

setup(
    author="{{ cookiecutter.author_full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.author_email }}",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
{%- set license_classifiers = {
    "MIT License": "License :: OSI Approved :: MIT License",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU General Public License v3.0": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "GNU General Public License v3.0 or later": "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "GNU General Public License v2.0": "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    "BSD 3-Clause 'New' or 'Revised' License": "License :: OSI Approved :: BSD License",
    "BSD 2-Clause 'Simplified' License": "License :: OSI Approved :: BSD License",
    "BSD License": "License :: OSI Approved :: BSD License",
    "GNU Lesser General Public License v2.1": "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
    "ISC License": "License :: OSI Approved :: ISC License (ISCL)",
} %}
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="{{ cookiecutter.project_description }}",  # noqa: E501
    setup_requires=[
        "setuptools-git",
    ],
    install_requires=requirements,
    extras_require={
        "dev": requirements_dev,
        "docs": requirements_docs,
    },
{%- set license_identifiers = {
    "MIT License": "MIT",
    "Apache Software License 2.0": "Apache-2.0",
    "GNU General Public License v3.0": "GPL-3.0-only",
    "GNU General Public License v3.0 or later": "GPL-3.0-or-later",
    "GNU General Public License v2.0": "GPL-2.0-only",
    "BSD 3-Clause 'New' or 'Revised' License": "BSD-3-Clause",
    "BSD 2-Clause 'Simplified' License": "BSD-2-Clause",
    "BSD License": "BSD-3-Clause",
    "GNU Lesser General Public License v2.1": "LGPL-2.1-only",
    "ISC License": "ISC",
    "Not open source": "Proprietary",
} %}
{%- if cookiecutter.open_source_license in license_identifiers %}
    license="{{ license_identifiers[cookiecutter.open_source_license] }}",
{%- endif %}
    long_description=readme + "\n\n" + history,
    name="{{ cookiecutter.python_package_name }}",
    packages=find_packages(include=["{{ cookiecutter.python_package_name }}", "{{ cookiecutter.python_package_name }}.*"]),
    include_package_data=True,
    test_suite="tests",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}",
    version="{{ cookiecutter.python_package_version }}",
    zip_safe=False,
)
