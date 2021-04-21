from setuptools import setup, find_packages
import os

PROJECT_NAME = "Matizla"
PROJECT_PACKAGE_NAME = "matizla"

PROJECT_GITHUB_USERNAME = "neotje"

PACKAGES = find_packages()

REQUIRED = [
    "pywebview==3.4",
    "pywebview[qt]==3.4",
    "pyqt5==5.15.4",
    "pyqtwebengine==5.15.4",
    "pycairo==1.20.0",
    "PyGObject==3.40.1"
]

setup(
    name=PROJECT_PACKAGE_NAME,
    packages=PACKAGES,
    install_requires=REQUIRED,
    entry_points={"console_scripts": [
        "matizla = matizla.__main__:main"]}
)