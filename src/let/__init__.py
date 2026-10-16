# flake8-in-file-ignores: noqa: F401,F403,F821

# Copyright (c) 2016 Taylor Marks
# Copyright (c) 2016 Adam Karpierz
# SPDX-License-Identifier: MIT

from __future__ import annotations

from .__about__ import * ; del __about__  # type: ignore[name-defined]

from ._let import * ; del _let  # type: ignore[name-defined]
