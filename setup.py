import io
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# ==============================================================================
# Utilities
# ==============================================================================


def read(path, encoding="utf-8"):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


setup(
    name="altair_examples",
    version="0.0.1-dev0",
    description="Examples for Altair.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Brian E. Granger / Jake VanderPlas / Jean-Daniel Fekete",
    author_email="jean-daniel.fekete@inria.fr",
    url="http://altair-viz.github.io",
    download_url="http://github.com/altair-viz/altair/",
    license="BSD 3-clause",
    packages=["altair_examples"],
    include_package_data=True,
    install_requires=["altair", "vega", "vega_datasets"],
    python_requires=">=3.7",
    extras_require={"dev": ["black", "ipython", "pytest"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
