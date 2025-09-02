# Copyright (c) 2016 Taylor Marks
# Copyright (c) 2016 Adam Karpierz
# SPDX-License-Identifier: MIT

__all__ = ('let',)

from typing import Any
import sys


def let(**name_value_pair: dict[str, Any]) -> Any:
    """Takes in a single name = value pair.

    The value is assigned to the name and returned.
    This is useful in if statements, while loops, and anyplace else
    where you want to both assign and use a value.

    Examples.

    Instead of:

        name = longInstanceName.longAttributeName
        if name:
            ...

    - Or worse, using that long identifier in the condition and then
    repeatedly in the body - you can use this:

        if let(name = longInstanceName.longAttributeName):
            ...

    Instead of:

        results = dbConnection.fetch_results():
        while results:
            ...
            results = dbConnection.fetch_results()

    You can do this:

        while let(results = dbConnection.fetch_results):
            ...

    Instead of:

        if len(sequence) != 1:
            raise Exception(f"Bad amount: {len(sequence)}")

    You could use:

        if let(count = len(sequence)) != 1:
            raise Exception(f"Bad amount: {count}")
    """
    count = len(name_value_pair)
    if count != 1:
        raise TypeError("let() takes exactly one key = value pair "
                        f"({count} given)")

    frame = sys._getframe(1)
    flocals  = frame.f_locals
    fglobals = frame.f_globals

    name, value = next(iter(name_value_pair.items()))
    if flocals is not fglobals and name in flocals:
        raise Exception(f"{name} has already been locally assigned. "
                        "Due to optimizations in the Python interpreter, "
                        "it is not possible to write over it using let(). "
                        "Sorry!")

    fglobals[name] = value
    return value
