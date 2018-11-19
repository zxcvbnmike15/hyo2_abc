import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.lib.testing import Testing

logger.debug("root folder: %s" % Testing.root_folder)
logger.debug("root data folder: %s" % Testing.root_data_folder())
logger.debug("input test files: %s" % Testing.input_test_files(ext=""))  # "" for files without extension
