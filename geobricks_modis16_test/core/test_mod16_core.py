import unittest
from geobricks_mod16.core import mod16_core as c


class GeobricksMod16Test(unittest.TestCase):

    def test_list_years(self):
        years = c.list_years()
        self.assertEqual(len(years), 15)
