#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
from enum import Enum, auto
from constants import AppMode, DataSources

class AppEnv(Enum):
    APP_ID   = (auto(), str, 'jfe')
    APP_NAME = (auto(), str, 'Jayh FastAPI Example')
    APP_MODE = (auto(), AppMode, AppMode.DEVELOPMENT.value)
    DATA_SOURCE = (auto(), DataSources, DataSources.CACHE.value)

    LOG_DIR     = (auto(), str, '')
    LOG_LEVEL   = (auto(), str, 'DEBUG') # FATAL, ERROR, WARN, INFO, DEBUG

    HOST = (auto(), str, '127.0.0.1')
    PORT = (auto(), int, 8080)

    PG_HOST = (auto(), str, '127.0.0.1')
    PG_PORT = (auto(), int, 5432)
    PG_USER = (auto(), str, 'jfe')
    PG_PASS = (auto(), str, 'jfe')
    PG_DATABASE = (auto(), str, 'jfe')

    def __init__(self, _, _value_type, _default_value):
        self.__key = self.name
        self.__value_type = _value_type
        self.__default_value = _default_value
    
    @property
    def key(self):
        return self.__key
    
    @property
    def value_type(self):
        return self.__value_type
    
    @property
    def default_value(self):
        return self.__default_value
    
    def get(self):
        if self.value_type == bool: return os.getenv(self.key, self.default_value).lower() in ['true', 't', '1']
        return self.value_type(os.getenv(self.key, self.default_value))
