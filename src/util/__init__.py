#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from appenv import AppEnv

from .applogger import AppLogger
logger = AppLogger(AppEnv.APP_ID.get())

