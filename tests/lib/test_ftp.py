import os
import unittest

from hyo2.abc.lib.ftp import Ftp
from hyo2.abc.lib.testing import Testing


class TestABCLibFtp(unittest.TestCase):

    def test_init(self):
        ftp = Ftp(host="ftp.ccom.unh.edu", password="test@gmail.com", show_progress=True, debug_mode=True)
        ftp.disconnect()

    def test_get_file(self):
        data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        testing = Testing(root_folder=data_folder)

        ftp = Ftp(host="ftp.ccom.unh.edu", password="test@gmail.com", show_progress=True, debug_mode=True)
        ftp.get_file(file_src="fromccom/hydroffice/Caris_Support_Files_5_5.zip",
                     file_dst=os.path.join(testing.output_data_folder(), "test.zip"))
        ftp.disconnect()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibFtp))
    return s
