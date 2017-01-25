#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python APRS Tracker Constants."""

import logging

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


LOG_LEVEL = logging.DEBUG
LOG_FORMAT = logging.Formatter(
    ('%(asctime)s aprstracker %(levelname)s %(name)s.%(funcName)s:%(lineno)d - '
     '%(message)s'))

GPS_WARM_UP = 5

NMEA_PROPERTIES = [
    'timestamp',
    'lat',
    'latitude',
    'lat_dir',
    'lon',
    'longitude',
    'lon_dir',
    'gps_qual',
    'mode_indicator',
    'num_sats',
    'hdop',
    'altitude',
    'horizontal_dil',
    'altitude_units',
    'geo_sep',
    'geo_sep_units',
    'age_gps_data',
    'ref_station_id',
    'pos_fix_dim',
    'mode_fix_type',
    'mode',
    'pdop',
    'vdop',
    'fix'
]
