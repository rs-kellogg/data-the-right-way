#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [
    "typer[all]",
    "rich",
    "shellingham",
    "awswrangler",
    "SQLAlchemy>=2.0.0rc2",
    "GeoAlchemy2",
    "boto3",
    "jinja2",
    "pyyaml",
    "pandas",
    "xmldict",
    "pyarrow",
    "pyodbc",
    "pymssql",
    "dask[all]",
    "dask-labextension",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Will Thompson",
    author_email="wkt@northwestern.edu",
    description="Data wrangling utiltiies",
    entry_points={
        "console_scripts": [
            "wrangler=wrangler.cli:app",
        ],
    },
    install_requires=requirements,
    include_package_data=True,
    keywords="wrangler",
    name="wrangler",
    packages=find_packages(
        include=["wrangler", "wrangler.*"]
    ),
    package_data={"wrangler": ["data/*"]},
    test_suite="tests",
    tests_require=test_requirements,
    version="0.1.0",
)
