import unittest

from loads.bins.no_aggregation_method import NoAggMethod


class TestNoAgg(unittest.TestCase):

    def test_init(self):
        tst = NoAggMethod()
        self.assertEqual(len(tst.loads), 0)

    def test_add_load(self):
        tst = NoAggMethod()
        tst.add_load(1)
        self.assertEqual(tst.loads[0].energy, 1)
