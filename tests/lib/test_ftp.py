import unittest

from hyo2.abc.lib.ftp import Ftp


class TestABCLibFtp(unittest.TestCase):

    def test_init(self):
        ftp = Ftp(host="http://ccom.unh.edu/ftp")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibFtp))
    return s
