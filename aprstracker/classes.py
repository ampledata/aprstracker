#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python APRS Tracker Class Definitions."""

import logging
import logging.handlers
import threading

import pynmea2

import aprs
import aprstracker

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


class SerialGPSPoller(threading.Thread):

    """Threadable Object for polling a serial NMEA-compatible GPS."""


    _logger = logging.getLogger(__name__)
    if not _logger.handlers:
        _logger.setLevel(aprstracker.LOG_LEVEL)
        _console_handler = logging.StreamHandler()
        _console_handler.setLevel(aprstracker.LOG_LEVEL)
        _console_handler.setFormatter(aprstracker.LOG_FORMAT)
        _logger.addHandler(_console_handler)
        _logger.propagate = False

    def __init__(self, serial_port, serial_speed):
        threading.Thread.__init__(self)
        self._serial_port = serial_port
        self._serial_speed = serial_speed
        self._stopped = False

        self.gps_props = {}
        for prop in aprstracker.NMEA_PROPERTIES:
            self.gps_props[prop] = None

        self._serial_int = serial.Serial(
            self._serial_port, self._serial_speed, timeout=1)

    def stop(self):
        """
        Stop the thread at the next opportunity.
        """
        self._stopped = True
        return self._stopped

    def run(self):
        streamreader = pynmea2.NMEAStreamReader(self._serial_int)
        try:
            while not self._stopped:
                for msg in streamreader.next():
                    for prop in aprstracker.NMEA_PROPERTIES:
                        if getattr(msg, prop, None) is not None:
                            self.gps_props[prop] = getattr(msg, prop)
                            self._logger.debug(
                                '%s=%s', prop, self.gps_props[prop])
        except StopIteration:
            pass

class LocationFrame(aprs.Frame):
    def __init__(self, frame=None):
        self.source = ''
        self.destination = 'APRS'
        self.path = []
        self.text = ''
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.course = None
        self.speed = None
        self.symboltable = None
        self.symbolcode = None
        self.comment = 'Python APRS Tracker'
        super(LocationFrame, self).__init__(frame)

    def make_frame(self):
        self.text = ''.join([
            '!',
            self.latitude,
            self.symboltable,
            self.longitude,
            self.symbolcode,
            "%03d" % self.course,
            '/',
            "%03d" % self.speed,
            '/',
            'A=',
            "%06d" % self.altitude,
            ' ',
            self.comment
        ])
