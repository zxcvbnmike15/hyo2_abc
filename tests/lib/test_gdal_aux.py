import os
import unittest

from hyo2.abc.lib.gdal_aux import GdalAux


class TestABCLibHelper(unittest.TestCase):

    def test_gdal_data(self):
        GdalAux.check_gdal_data()

    def test_crs_id(self):
        wkt = """
        GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]
        """
        self.assertEqual(GdalAux.crs_id(wkt=wkt), "4326")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibHelper))
    return s
