#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

from enum import Enum

class AppMode(Enum):
    DEVELOPMENT = 'dev'
    PRODUCTION = 'prod'

    @classmethod
    def _missing_(cls, value):
        return AppMode.DEVELOPMENT

class DataSources(Enum):
    CACHE = 'cache'
    POSTGRESQL = 'postgresql'

    @classmethod
    def _missing_(cls, value):
        return DataSources.CACHE

ITEM_IN_SCHEMA = True
