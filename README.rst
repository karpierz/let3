let3
====

Assign variables wherever, whenever you want.

Overview
========

|package_bold| is a strict fork of Taylor Marks's let_ package with a fix
allowing to work with Python3 or higher and with a little code reformatting
and minor improvements.

`PyPI record`_.

`Documentation`_.

Overview below is a copy from the original let_ website (with only the necessary
changes regarding |package|).

Quick Start
-----------
Once you've installed, you can really quickly verified that it works with just this:

.. code-block:: python

    >>> from let import let
    >>> if let(count = len("Hello World!")):
    ...     print(count)
    12

Documentation
-------------
In C, Java, and many other languages, it's possible to assign variables inside
of if or while condition statements. This is useful in allowing you to concisely
both assign the value, and check whether a condition is met.

This ability doesn't exist in Python, because of the thought that when people
write something like:

.. code-block:: python

    if row = db.fetch_results():
        ...

They may have actually meant:

.. code-block:: python

    if row == db.fetch_results():
        ...

Personally, I have never made this mistake. It seems far more like a theoretical
mistake that could plausibly happen than one that actually happens and warrants
removing features, as was chosen in Python.

Anyways, the let function in this module gives you something very close to that
ability in other languages. A few examples:

.. code-block:: python

    if let(name = longInstanceName.longAttributeName):
        ...

    # Yes, db.fetch_results() should just return a generator. No, it doesn't.
    while let(results = db.fetch_results()):
        ...

    if let(count = len(nameValuePair)) != 1:
        raise Exception(f"Bad amount: {count}")

Installation
============

Prerequisites:

+ Python 3.10 or higher

  * https://www.python.org/

+ pip and setuptools

  * https://pypi.org/project/pip/
  * https://pypi.org/project/setuptools/

To install run:

  .. parsed-literal::

    python -m pip install --upgrade |package|

Development
===========

Prerequisites:

+ Development is strictly based on *tox*. To install it run::

    python -m pip install --upgrade tox

Visit `Development page`_.

Installation from sources:

clone the sources:

  .. parsed-literal::

    git clone |respository| |package|

and run:

  .. parsed-literal::

    python -m pip install ./|package|

or on development mode:

  .. parsed-literal::

    python -m pip install --editable ./|package|

License
=======

  | |copyright|
  | Copyright (c) 2016 Taylor Marks
  | Licensed under the MIT License
  | https://opensource.org/license/mit
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Taylor Marks <taylor@marksfam.com>
* Adam Karpierz <adam@karpierz.net>

.. |package| replace:: let3
.. |package_bold| replace:: **let3**
.. |copyright| replace:: Copyright (c) 2016-2025 Adam Karpierz
.. |respository| replace:: https://github.com/karpierz/let3.git
.. _Development page: https://github.com/karpierz/let3
.. _PyPI record: https://pypi.org/project/let3/
.. _Documentation: https://let3.readthedocs.io/
.. _let: https://pypi.org/project/let/
