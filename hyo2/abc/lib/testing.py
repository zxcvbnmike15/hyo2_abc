import os
from typing import Optional
import logging
logger = logging.getLogger(__name__)


class Testing:
    """A collection of methods to input/output test folders/files.

    Just set the root_folder for use with different packages.
    """

    def __init__(self, root_folder: Optional[str]=None):

        if root_folder is None:
            self.root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
        else:
            if not os.path.exists(root_folder):
                raise RuntimeError("passed invalid root folder: " % root_folder)
            self.root_folder = root_folder

    # --- FOLDERS ---

    def root_data_folder(self) -> str:
        data_folder = os.path.abspath(os.path.join(self.root_folder, 'data'))
        if not os.path.exists(data_folder):
            raise RuntimeError("the root test data folder does not exist: %s" % data_folder)
        return data_folder

    def input_data_folder(self) -> str:
        folder = os.path.abspath(os.path.join(self.root_data_folder(), 'input'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def download_data_folder(self) -> str:
        folder = os.path.abspath(os.path.join(self.root_data_folder(), 'download'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def temp_data_folder(self) -> str:
        folder = os.path.abspath(os.path.join(self.root_data_folder(), 'temp'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def output_data_folder(self) -> str:
        folder = os.path.abspath(os.path.join(self.root_data_folder(), 'output'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    # -- FILES ---

    @classmethod
    def files(cls, folder: str, ext: str, subfolder: Optional[str]=None) -> list:
        file_list = list()
        for root, _, files in os.walk(folder):

            # logger.info("root: %s, folder: %s" % (root, subfolder))
            if subfolder is not None:
                if subfolder not in root:
                    continue

            for f in files:
                if f.endswith(ext):
                    file_list.append(os.path.join(root, f))
        return file_list

    def input_test_files(self, ext: str, subfolder: Optional[str]=None) -> list:
        return self.files(folder=self.input_data_folder(), ext=ext, subfolder=subfolder)

    def download_test_files(self, ext: str, subfolder: Optional[str]=None) -> list:
        return self.files(folder=self.download_data_folder(), ext=ext, subfolder=subfolder)

    def temp_test_files(self, ext: str, subfolder: Optional[str]=None) -> list:
        return self.files(folder=self.temp_data_folder(), ext=ext, subfolder=subfolder)

    def output_test_files(self, ext: str, subfolder: Optional[str]=None) -> list:
        return self.files(folder=self.output_data_folder(), ext=ext, subfolder=subfolder)
