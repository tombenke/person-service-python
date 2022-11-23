import os
import pathlib
from setuptools import find_packages, setup

# Package metadata
# ----------------
APP_NAME = "person-service-python"
APP_DESCRIPTION = """A sample easer REST API endpoint implementation in Python"""

# Get the long description from the README file
HERE = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")

URL = "https://github.com/lhsystems/person-service-python"
EMAIL = "tamas.benke@lhsystems.com"
AUTHOR = "Tamás Benke"
LICENSE = "LSY"
REQUIRES_PYTHON = ">=3.8"

# What packages are required for this module to be executed?
REQUIRED = [
    "argparse",
    "py-12f-common >= 0.6.0",
    "datetime",
    "dataclasses",
    "environs",
    "loguru",
    "otel-inst-py >= 2.0.0",
    "python-dotenv",
    "py-msgp >= 1.0.0",
    "protobuf <= 3.19.4",
    "uuid",
]

DEV_REQUIREMENTS = [
    "coverage",
    "coverage-badge",
    "black",
    "pdoc",
    "pydeps",
    "pylint",
    "pyinstaller",
]

setup(
    name=APP_NAME,
    version=os.getenv("VERSION", "1.0.0"),
    description=APP_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    license=LICENSE,
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=REQUIRED,
    extras_require={"dev": DEV_REQUIREMENTS},
    entry_points={
        "console_scripts": [
            "person-service-python = app.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
