import os
from typing import Optional
import logging
logger = logging.getLogger(__name__)


class Testing:
    """A collection of class methods to input/output test folders/files.

    Just set the root_folder for use with different packages.
    """

    root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))

    # --- FOLDERS ---

    @classmethod
    def root_data_folder(cls) -> str:
        data_folder = os.path.abspath(os.path.join(cls.root_folder, 'data'))
        if not os.path.exists(data_folder):
            raise RuntimeError("the root test data folder does not exist: %s" % data_folder)
        return data_folder

    @classmethod
    def input_data_folder(cls) -> str:
        folder = os.path.abspath(os.path.join(cls.root_data_folder(), 'input'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    @classmethod
    def download_data_folder(cls) -> str:
        folder = os.path.abspath(os.path.join(cls.root_data_folder(), 'download'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    @classmethod
    def temp_data_folder(cls) -> str:
        folder = os.path.abspath(os.path.join(cls.root_data_folder(), 'temp'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    @classmethod
    def output_data_folder(cls) -> str:
        folder = os.path.abspath(os.path.join(cls.root_data_folder(), 'output'))
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

    @classmethod
    def input_test_files(cls, ext: str, subfolder: Optional[str]=None) -> list:
        return cls.files(folder=cls.input_data_folder(), ext=ext, subfolder=subfolder)

    @classmethod
    def download_test_files(cls, ext: str, subfolder: Optional[str]=None) -> list:
        return cls.files(folder=cls.download_data_folder(), ext=ext, subfolder=subfolder)

    @classmethod
    def temp_test_files(cls, ext: str, subfolder: Optional[str]=None) -> list:
        return cls.files(folder=cls.temp_data_folder(), ext=ext, subfolder=subfolder)

    @classmethod
    def output_test_files(cls, ext: str, subfolder: Optional[str]=None) -> list:
        return cls.files(folder=cls.output_data_folder(), ext=ext, subfolder=subfolder)
