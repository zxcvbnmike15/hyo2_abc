import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.lib.helper import Helper
from hyo2.abc.lib.lib_info import LibInfo

h = Helper(lib_info=LibInfo())

logger.debug("lib info:\n%s" % h.package_info())
