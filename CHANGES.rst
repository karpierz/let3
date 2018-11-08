Changelog
=========

1.0.9 (2018-11-08)
------------------
  - Drop support for Python 2.6 and 3.0-3.3
  - Update required setuptools version.

1.0.8 (2018-05-08)
------------------
  - Update required setuptools version.
  - Improve and simplify setup and packaging.

1.0.7 (2018-02-26)
------------------
  - Improve and simplify setup and packaging.

1.0.6 (2018-01-28)
------------------
  - Fix a bug and inconsistencies in tox.ini
  - Update of README.rst.

1.0.3 (2018-01-24)
------------------
  - Update required Sphinx version.
  - Update doc Sphinx configuration files.

1.0.2 (2017-11-18)
------------------
  - Setup improvements.
  - Other minor improvements.

1.0.1 (2017-01-05)
------------------
  - Creating a fork of Taylor Marks's *let* package with a fix allowing
    to work with Python3 or higher.
  - Minor improvements.

Changes of the original *let*:

1.0.1 (Feb 25, 2016)
--------------------
  - Let now assigns the variables to the global namespace always - never
    the local namespace. The Python interpreter sometimes optimizes variables
    within the local namespace - it's best not to change values behind its
    back, as it leads to very difficult to discover bugs.

1.0.0 (Feb. 7, 2016)
--------------------
  - Initial commit
