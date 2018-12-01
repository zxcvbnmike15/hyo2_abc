import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.lib.helper import Helper
from hyo2.abc.lib.lib_info import LibInfo

h = Helper(lib_info=LibInfo())

logger.debug("lib info:\n%s" % h.package_info())

logger.debug("is Pydro: %s" % Helper.is_pydro())

if Helper.is_pydro():
    logger.debug("HSTB folder: %s" % Helper.hstb_folder())
    logger.debug("atlases folder: %s" % Helper.hstb_atlases_folder())
    logger.debug("WOA09 folder: %s" % Helper.hstb_woa09_folder())
    logger.debug("WOA13 folder: %s" % Helper.hstb_woa13_folder())
