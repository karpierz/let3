# coding: utf-8

__all__ = ('__title__', '__summary__', '__uri__', '__version_info__',
           '__version__', '__author__', '__email__', '__copyright__',
           '__license__')

__title__        = "let3"
__summary__      = "Assign variables wherever, whenever you want"
__uri__          = "http://pypi.python.org/pypi/let3/"
__version_info__ = type("version_info", (), dict(serial=0,
                        major=1, minor=0, micro=1, releaselevel="final"))
__version__      = "{0.major}.{0.minor}.{0.micro}".format(__version_info__)
__author__       = "Adam Karpierz"
__email__        = "python@python.pl"
__copyright__    = "Copyright (c) 2017 {0}".format(__author__)
__license__      = "MIT License ; https://opensource.org/licenses/MIT"

# eof
