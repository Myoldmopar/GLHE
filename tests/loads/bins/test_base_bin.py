import unittest

from loads.bins.base_bin import BaseBin


class TestDynamic(unittest.TestCase):

    def test_init(self):
        tst = BaseBin()
        self.assertEqual(tst.energy, 0)
        self.assertEqual(tst.width, 0)

    def test_get_load(self):
        tst = BaseBin(energy=1, width=1)
        self.assertEqual(tst.get_load(), 1)
