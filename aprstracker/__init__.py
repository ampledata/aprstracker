#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python APRS Tracker.

"""
Python APRS Tracker.
~~~~


:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2017 Greg Albrecht
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/aprs>

"""

from .constants import (LOG_FORMAT, LOG_LEVEL, NMEA_PROPERTIES,  # NOQA
                        GPS_WARM_UP)

from .classes import SerialGPSPoller  # NOQA

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'
