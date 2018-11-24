import gdal
import ogr
import osr

from typing import Optional
import os
import logging

logger = logging.getLogger(__name__)

from hyo2.abc.lib.helper import Helper


class GdalAux:
    """ Auxiliary class to manage GDAL stuff """

    error_loaded = False
    data_fixed = False

    @classmethod
    def gdal_error_handler(cls, err_class, err_num, err_msg) -> None:
        """GDAL Error Handler, to test it: gdal.Error(1, 2, b'test error')"""

        err_type = {
            gdal.CE_None: 'None',
            gdal.CE_Debug: 'Debug',
            gdal.CE_Warning: 'Warning',
            gdal.CE_Failure: 'Failure',
            gdal.CE_Fatal: 'Fatal'
        }
        err_msg = err_msg.replace('\n', ' ')
        err_class = err_type.get(err_class, 'None')

        raise RuntimeError("%s: gdal error %s > %s" % (err_class, err_num, err_msg))

    @classmethod
    def push_gdal_error_handler(cls) -> None:
        """ Install GDAL error handler """
        if cls.error_loaded:
            return

        gdal.PushErrorHandler(cls.gdal_error_handler)

        gdal.UseExceptions()
        ogr.UseExceptions()
        osr.UseExceptions()

        cls.error_loaded = True

    @classmethod
    def check_gdal_data(cls):
        """ Check the correctness of os env GDAL_DATA """

        if cls.data_fixed:
            return

        if 'GDAL_DATA' in os.environ:

            logger.debug("unset original GDAL_DATA = %s" % os.environ['GDAL_DATA'])
            del os.environ['GDAL_DATA']

        gdal_data_path1 = os.path.join(os.path.dirname(gdal.__file__), 'data', 'gdal')
        gcs_csv_path1 = os.path.join(gdal_data_path1, 'gcs.csv')
        if os.path.exists(gcs_csv_path1):

            gdal.SetConfigOption('GDAL_DATA', gdal_data_path1)
            logger.debug("resulting GDAL_DATA = %s" % gdal.GetConfigOption('GDAL_DATA'))
            cls.data_fixed = True
            cls.push_gdal_error_handler()
            return

        # anaconda specific (Win)
        gdal_data_path2 = os.path.join(Helper.python_path(), 'Library', 'data')
        gcs_csv_path2 = os.path.join(gdal_data_path2, 'gcs.csv')
        if os.path.exists(gcs_csv_path2):

            gdal.SetConfigOption('GDAL_DATA', gdal_data_path2)
            logger.debug("resulting GDAL_DATA = %s" % gdal.GetConfigOption('GDAL_DATA'))
            cls.data_fixed = True
            cls.push_gdal_error_handler()
            return

        # anaconda specific (Win)
        gdal_data_path3 = os.path.join(Helper.python_path(), 'Library', 'share', 'gdal')
        gcs_csv_path3 = os.path.join(gdal_data_path3, 'gcs.csv')
        if os.path.exists(gcs_csv_path3):

            gdal.SetConfigOption('GDAL_DATA', gdal_data_path3)
            logger.debug("resulting GDAL_DATA = %s" % gdal.GetConfigOption('GDAL_DATA'))
            cls.data_fixed = True
            cls.push_gdal_error_handler()
            return

        # anaconda specific (Linux)
        gdal_data_path4 = os.path.join(Helper.python_path(), 'share', 'gdal')
        gcs_csv_path4 = os.path.join(gdal_data_path4, 'gcs.csv')
        if os.path.exists(gcs_csv_path4):

            gdal.SetConfigOption('GDAL_DATA', gdal_data_path4)
            logger.debug("resulting GDAL_DATA = %s" % gdal.GetConfigOption('GDAL_DATA'))
            cls.data_fixed = True
            cls.push_gdal_error_handler()
            return

        # TODO: add more cases to find GDAL_DATA

        raise RuntimeError("Unable to locate GDAL data at:\n- %s\n- %s\n- %s\n- %s"
                           % (gdal_data_path1, gdal_data_path2, gdal_data_path3, gdal_data_path4))

    @classmethod
    def crs_id(cls, wkt: str) -> Optional[int]:
        srs = osr.SpatialReference()
        srs.ImportFromWkt(wkt)
        srs.AutoIdentifyEPSG()
        return srs.GetAuthorityCode(None)
