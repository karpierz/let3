# coding: utf-8

from __future__ import absolute_import
import sys, os
test_dir = os.path.dirname(os.path.abspath(__file__))
top_dir  = os.path.dirname(test_dir)
if top_dir not in sys.path: sys.path.insert(0, top_dir)
del sys, os

# eof
