from setuptools import setup, find_packages
import sys
import os

sys.path.append(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "PyFlow", "Core")
)
from version import currentVersion

setup(
    name="PyFlow",
    version=str(currentVersion()),
    packages=find_packages(),
    entry_points={"console_scripts": ["pyflow = PyFlow.Scripts:main"]},
    include_package_data=True,
    author="Ilgar Lunin, Pedro Cabrera",
    author_email="pedro.c.vfx@gmail.com",
    description="A general purpose runtime extendable python qt node editor.",
    keywords="visual programming framework",
    url="https://pedrocabrera.github.io/PyFlow/",  # project home page
    project_urls={
        "Bug Tracker": "https://github.com/pedrocabrera/PyFlow/issues",
        "Documentation": "https://pyflow.readthedocs.io",
        "Source Code": "https://github.com/pedrocabrera/PyFlow",
    },
    classifiers=["License :: Appache-2.0"],
    install_requires=[
        "PySide6",
        "qtpy",
        "blinker",
        "docutils",
        "SQLAlchemy",
        "requests",
    ],
)
