import unittest
from geobricks_mod16.core import mod16_core as c


class GeobricksMod16Test(unittest.TestCase):

    def test_list_layers(self):
        out = c.list_layers('PET')
        self.assertEqual(len(out), 180)
        out = c.list_layers('ET')
        self.assertEqual(len(out), 180)

    # def test_download(self):
    #     c.download('ET')
