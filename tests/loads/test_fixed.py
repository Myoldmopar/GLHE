import unittest

from loads.loadProfile.fixed import Fixed


class TestFixed(unittest.TestCase):

    def test_get_load(self):
        tst = Fixed(1)
        self.assertEqual(tst.get_load(), 1)
