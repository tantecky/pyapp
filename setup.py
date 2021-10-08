from setuptools import setup, find_packages
from pyapp import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyapp",
    version=__version__,
    author="tantecky",
    author_email="tantecky@seznam.cz",
    description="An example app in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantecky/pyapp",
    license="MIT",
    install_requires=[
        "numpy",
        "PySide6",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-html",
            "autopep8",
            "autoflake",
            "black",
            "isort",
            "mypy",
            "tox",
            "flake8",
            "coverage",
        ]
    },
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.8",
    entry_points={
        "gui_scripts": [
            "pyapp=pyapp.gui:show",
        ]
    },
)
