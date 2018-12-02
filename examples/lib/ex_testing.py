import logging

from hyo2.abc.lib.testing import Testing

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

t = Testing()

logger.debug("root folder: %s" % t.root_folder)
logger.debug("root data folder: %s" % t.root_data_folder())
logger.debug("input test files: %s" % t.input_test_files(ext=""))  # "" for files without extension
