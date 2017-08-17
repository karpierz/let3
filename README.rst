let3
====

*Assign variables wherever, whenever you want.*

Overview
========

  *let3* is a strict fork of Taylor Marks's let_ package with a fix allowing
  to work with Python3 or higher and with a little code reformatting and
  minor improvements.

  Overview below is a copy from the original let_ website (with only the
  necessary changes regarding let3).

Installation
------------
Install via pip:

.. code-block:: bash

    $ pip install --upgrade let3

Done.

Quick Start
-----------
Once you've installed, you can really quickly verified that it works with just this:

.. code-block:: python

    >>> from let import let
    >>> if let(count = len('Hello World!')):
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
        raise Exception('Bad amount: {}'.format(count))

Installation prerequisites
==========================

+ Python 2.6 or higher

  * http://www.python.org/
  * 2.7 and 3.4 are primary test environments.

+ pip or setuptools

  * http://pypi.python.org/pypi/pip
  * http://pypi.python.org/pypi/setuptools

License
=======

  | Licensed under the MIT License
  | https://opensource.org/licenses/MIT
  | Please refer to the bundled LICENSE file.

Authors
=======

* Taylor Marks <taylor@marksfam.com>
* Adam Karpierz <python@python.pl>

.. _let: http://pypi.python.org/pypi/let/