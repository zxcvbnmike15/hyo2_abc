import logging
import os.path

from hyo2.abc.lib.logging import set_logging
from hyo2.abc.lib.testing import Testing
from hyo2.abc.lib.onedrive import OneDrive

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc"])

# onedrive_link = r"https://universitysystemnh-my.sharepoint.com/:u:/g/personal/" \
#                 r"gma72_usnh_edu/EaMqI1w9pplDsqCapeqJYYgBo0LP8CqHnkyXlDKkoHeBLg?e=4MEVzV&download=1"
onedrive_link = r"https://universitysystemnh-my.sharepoint.com/:u:/g/personal/" \
                r"gma72_usnh_edu/ET4kv3t8CuBGuyHUqThonvMBMmxWp5f3ZTt08XG_u9COHQ?e=mVEJij&download=1"

file_dst = os.path.join(Testing().output_data_folder(), "onedrive.zip")

od = OneDrive(show_progress=True, debug_mode=True)
od.get_file(file_src=onedrive_link, file_dst=file_dst, unzip_it=True)
