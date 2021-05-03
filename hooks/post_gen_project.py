#!/usr/bin/env python
import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path(".").absolute()


def remove(filepath):
    target = PROJECT_DIRECTORY / filepath

    if target.is_dir():
        shutil.rmtree(target, ignore_errors=True)
    else:
        target.unlink()


def remove_license_if_neccesary():
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove("LICENSE")


def remove_licenses():
    remove("licenses")


def remove_requirements_txt():
    remove("requirements_poetry")
    remove("requirements_setuptools")


def main():
    remove_license_if_neccesary()
    remove_licenses()
    remove_requirements_txt()


if __name__ == "__main__":
    main()
