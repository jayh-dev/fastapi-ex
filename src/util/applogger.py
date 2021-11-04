#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os, sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

from appenv import AppEnv

class AppLogger(object):
    def __init__(self, name=None):
        self.__name = name if name else 'default'
        _formatter = logging.Formatter('[%(asctime)s|%(name)s|%(levelname)s] %(message)s')
        _level = AppEnv.LOG_LEVEL.get()

        self.__logger = logging.getLogger(self.__name)
        if _level == 'ERROR': self.__logger.setLevel(logging.ERROR)
        elif _level == 'WARN': self.__logger.setLevel(logging.WARN)
        elif _level == 'INFO': self.__logger.setLevel(logging.INFO)
        else: self.__logger.setLevel(logging.DEBUG)
        
        # stream handler
        _stream_handler = logging.StreamHandler()
        _stream_handler.setFormatter(_formatter)
        self.__logger.addHandler(_stream_handler)

        # file handler
        _log_dir = AppEnv.LOG_DIR.get()
        if _log_dir:
            if not os.path.exists(_log_dir) or not os.path.isdir(_log_dir):
                os.makedirs(_log_dir)
            _file_handler = RotatingFileHandler(f'{_log_dir}/last.log', maxBytes=1024*1024*10, backupCount=10)
            _file_handler.setFormatter(_formatter)
            self.__logger.addHandler(_file_handler)
        
    def __message(self, *args):
        return ' '.join(self.__message(*v) if type(v) in [tuple] else str(v) for v in args)
    
    def d(self, *args):
        self.__logger.debug(self.__message(args))

    def i(self, *args):
        self.__logger.info(self.__message(args))

    def w(self, *args, trace=True):
        _, error, tb = sys.exc_info()
        self.__logger.warning(self.__message(args), exc_info=trace and (error or tb))

    def e(self, *args, trace=True):
        _, error, tb = sys.exc_info()
        self.__logger.error(self.__message(args), exc_info=1 if trace else 0)
    
    def trace(self):
        def show(msg):
            print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]}|{self.__name}|TRACE] {msg}')
        _, error, tb = sys.exc_info()
        
        if tb:
            show(f'File {tb.tb_frame.f_code.co_filename}, line {tb.tb_lineno}, in {tb.tb_frame.f_code.co_name} : {error}')
        else:
            show('No Traceback')
