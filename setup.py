from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyapp",
    version="0.0.1",
    author="tantecky",
    author_email="tantecky@seznam.cz",
    description="An example app in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantecky/pyapp",
    license="MIT",
    install_requires=["numpy"],
    extras_require={
        "dev": [
            "pytest",
            "pytest-html",
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
)
