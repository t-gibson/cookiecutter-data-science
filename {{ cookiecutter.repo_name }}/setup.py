from distutils.util import convert_path
from setuptools import find_packages, setup

main_ns = {}
ver_path = convert_path("src/core/version.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

requirements = [
    "Click"
]

setup(
    name='core',
    version=main_ns["__version__"],
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    packages = find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["core=core.cli:main"]},
    install_requires=requirements,
    test_suite="tests",
)
