from setuptools import find_packages, setup

VERSION = "3.0.2"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-boxes.svg
    :target: https://pypi.python.org/pypi/pinax-boxes/

===========
Pinax Boxes
===========

.. image:: https://img.shields.io/pypi/v/pinax-boxes.svg
    :target: https://pypi.python.org/pypi/pinax-boxes/

\ 

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-boxes.svg
    :target: https://circleci.com/gh/pinax/pinax-boxes
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-boxes.svg
    :target: https://codecov.io/gh/pinax/pinax-boxes
.. image:: https://img.shields.io/github/contributors/pinax/pinax-boxes.svg
    :target: https://github.com/pinax/pinax-boxes/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-boxes.svg
    :target: https://github.com/pinax/pinax-boxes/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-boxes.svg
    :target: https://github.com/pinax/pinax-boxes/pulls?q=is%3Apr+is%3Aclosed

\ 

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\ 

``pinax-boxes`` is an app for including boxes of admin-controllable content in templates.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
|  1.11           |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
|  2.0            |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="An app for including boxes of admin-controllable content in templates.",
    name="pinax-boxes",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-boxes/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "boxes": []
    },
    install_requires=[
        "django-appconf>=1.0.1"
    ],
    tests_require=[
    ],
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
