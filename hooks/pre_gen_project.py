#!/usr/bin/env python
import re
import sys


def check_module_name():
    module_regex = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
    module_name = "{{ cookiecutter.python_package_name }}"

    if not re.match(module_regex, module_name):
        print(
            "ERROR: The package name (%s) is not a valid Python module name. Please do not use a - and use _ instead"
            % module_name,
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    check_module_name()


if __name__ == "__main__":
    main()
