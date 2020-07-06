from setuptools import setup, find_namespace_packages, find_packages

import re
VERSIONFILE="example_project/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="example_project",
    version=verstr,
    author="Joel Thomas",
    author_email="joelcthomas.com",
    description="An example project template to showcase how to structure a productive data science project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joelcthomas/productive-datascience-template",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)