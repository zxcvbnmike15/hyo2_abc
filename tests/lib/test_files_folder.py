import os
import unittest

from hyo2.abc.lib.testing import Testing


class TestABCLibTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Testing.root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                           os.pardir, os.pardir))

    def test_root_folder(self):
        self.assertTrue(os.path.exists(Testing.root_folder))
        self.assertGreater(len(Testing.files(folder=Testing.root_folder, ext="")), 0)

    def test_input_data(self):
        self.assertTrue(os.path.exists(Testing.input_data_folder()))
        self.assertGreater(len(Testing.input_test_files(ext="")), 0)

    def test_download_data(self):
        self.assertTrue(os.path.exists(Testing.download_data_folder()))
        self.assertGreaterEqual(len(Testing.download_test_files(ext="")), 0)

    def test_temp_data(self):
        self.assertTrue(os.path.exists(Testing.temp_data_folder()))
        self.assertGreaterEqual(len(Testing.temp_test_files(ext="")), 0)

    def test_output_data(self):
        self.assertTrue(os.path.exists(Testing.output_data_folder()))
        self.assertGreaterEqual(len(Testing.output_test_files(ext="")), 0)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibTesting))
    return s
