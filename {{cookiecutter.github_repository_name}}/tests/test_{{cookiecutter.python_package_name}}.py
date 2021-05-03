from {{ cookiecutter.python_package_name }} import __version__


def test_version():
    assert __version__ == "{{ cookiecutter.python_package_version }}"
