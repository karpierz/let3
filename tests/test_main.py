# Copyright (c) 2016 Adam Karpierz
# SPDX-License-Identifier: MIT

import unittest

import let
from let import let


class MainTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):

        let(count0 = len(["one"]))
        self.assertEqual(count0, 1)

        if let(count1 = len(["one"])) != 1:
            raise ValueError(f"Bad amount: {count1}")  # pragma: no cover
        self.assertEqual(count1, 1)

        with self.assertRaises(ValueError):
            if let(count2 = len([])) != 1:  # pragma: no cover
                raise ValueError(f"Bad amount: {count2}")

        with self.assertRaisesRegex(TypeError,
                                    r"^let\(\) takes 0 positional arguments but 1 was given"):
            let("value")

        with self.assertRaisesRegex(TypeError,
                                    r"^let\(\) takes exactly one key = value pair \(0 given\)"):
            let()

        with self.assertRaisesRegex(TypeError,
                                    r"^let\(\) takes exactly one key = value pair \(2 given\)"):
            let(name1 = "value1",
                name2 = "value2")

        name3 = "dummy"
        with self.assertRaisesRegex(Exception,
                                    r"^name3 has already been locally assigned. *"):
            let(name3 = "value3")

        it = iter(["OK", "OK", "OK", "OK", "OK", "OK", "OK", None])
        while let(result = next(it)):
            self.assertEqual(result, "OK")
