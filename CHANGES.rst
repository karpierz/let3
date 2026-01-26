Changelog
=========

2.1.1 (2026-01-26)
------------------
- Marked the package as typed.
- Copyright year update.
- Switched from tox to Nox for project automation.
- The documentation has been moved from Read the Docs to GitHub Pages.
- Added the nox's 'cleanup' test environment.
- Setup update (mainly dependencies) and bug fixes.

1.4.0 (2025-09-01)
------------------
- Made the package typed.
- Setup update (mainly dependencies).

1.2.3 (2025-07-07)
------------------
- Setup update (mainly dependencies).

1.2.2 (2025-05-15)
------------------
- The distribution is now built using 'build' instead of 'setuptools'.
- Setup update (mainly dependencies) (due to regressions in tox and setuptools).

1.2.1 (2025-05-04)
------------------
- Setup update (mainly dependencies).

1.2.0 (2025-04-28)
------------------
- Added support for Python 3.14
- Dropped support for Python 3.9 (due to compatibility issues).
- Updated Read the Docs' Python version to 3.13
- Updated tox's base_python to version 3.13
- Setup update (mainly dependencies).

1.1.7 (2025-03-20)
------------------
- Added support for PyPy 3.11
- Dropped support for PyPy 3.9
- Setup update (mainly dependencies).

1.1.5 (2025-02-14)
------------------
- Setup update (mainly dependencies).

1.1.4 (2025-01-20)
------------------
- Copyright year update.
- Setup update (mainly dependencies).

1.1.3 (2024-12-13)
------------------
- Source distribution (\*.tar.gz now) is compliant with PEP-0625.
- Add unittests.
- 100% code linting.
- 100% code coverage.
- Tox configuration is now in native (toml) format.
- Setup update (mainly dependencies).

1.1.2 (2024-10-30)
------------------
- Setup update (mainly dependencies).

1.1.1 (2024-10-09)
------------------
- Setup update (mainly dependencies).

1.1.0 (2024-09-30)
------------------
- Dropped support for Python 3.8
- Setup update (mainly dependencies).

1.0.25 (2024-08-13)
-------------------
- Added support for Python 3.13
- Setup update (mainly dependencies).

1.0.24 (2024-01-30)
-------------------
- Setup update (now based on tox >= 4.0).
- Added support for Python 3.12
- Dropped support for Python 3.7
- Added support for PyPy 3.9 and 3.10
- Added support for PyPy 3.7 and 3.8
- Copyright year update.
- The tox configuration has been moved to pyproject.toml
- Cleanup.

1.0.20 (2022-08-22)
-------------------
- Added support for Python 3.10 and 3.11
- Setup update (currently based mainly on pyproject.toml).

1.0.19 (2022-01-10)
-------------------
- Dropped support for Python 3.6.
- Copyright year update.
- Setup update.

1.0.17 (2021-10-14)
-------------------
- Setup update.

1.0.16 (2021-07-19)
-------------------
- Bugfix: 'let' works now also on highest (e.g. module) level.
- Setup general update and improvement.

1.0.15 (2020-10-17)
-------------------
- Added support for Python 3.8 and 3.9.
- Dropped support for Python 3.5.
- Dropped support for Python 2.
- Setup: fix an improper dependencies versions.
- Setup general update and cleanup.
- Fixed docs setup.
- Cleanup.

1.0.10 (2019-05-21)
-------------------
- Update required setuptools version.
- Setup update and improvements.
- This is the latest release that supports Python 2.

1.0.9 (2018-11-08)
------------------
- Dropped support for Python 2.6 and 3.0-3.3
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
