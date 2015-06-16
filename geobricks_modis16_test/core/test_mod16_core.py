import unittest
from geobricks_mod16.core import mod16_core as c


class GeobricksMod16Test(unittest.TestCase):

    def test_list_years(self):
        out = c.list_years()
        self.assertEqual(len(out), 15)

    def test_list_days(self):
        out = c.list_days(2014)
        self.assertEqual(len(out), 46)
