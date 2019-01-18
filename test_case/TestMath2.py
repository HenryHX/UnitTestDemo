#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from base.MathFunc import *


class TestMathFunc(unittest.TestCase):

    def test_multi(self):
        '''乘'''
        self.assertEqual(6, multi(3, 2))

    def test_divide(self):
        '''除'''
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    unittest.main()
