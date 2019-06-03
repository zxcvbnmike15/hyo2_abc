import logging

from hyo2.abc.lib.testing_paths import TestingPaths
from hyo2.abc.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc"])

tp = TestingPaths()

logger.debug("root folder: %s" % tp.root_folder)
logger.debug("root data folder: %s" % tp.root_data_folder())
logger.debug("input test files: %s" % tp.input_test_files(ext=""))  # "" for files without extension
