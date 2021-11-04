#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import session, sessionmaker

from appenv import AppEnv
from util import AppLogger

class Helper(object):
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def __init__(self, logger: AppLogger = None) -> None:
        self.__logger__ = logger if logger else AppLogger('PG')
        __URL = 'postgresql://{}:{}@{}:{}/{}'.format(
            AppEnv.PG_USER.get(), AppEnv.PG_PASS.get(), AppEnv.PG_HOST.get(), AppEnv.PG_PORT.get(), AppEnv.PG_DATABASE.get()
        )
        __CONF = {
            'encoding': 'utf-8',
            'pool_size': 10,
            'pool_pre_ping': True,
        }

        self.__engine__: engine.Engine = create_engine(__URL, **__CONF)
        self.logger.i('** PG Info:', self.engine)
        self.__session__ = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    
    @property
    def engine(self) -> engine.Engine:
        return self.__engine__
    
    @property
    def session(self) -> session.Session:
        ret: session.Session = self.__session__()
        ret.autoflush = False
        ret.autocommit = False
        return ret
    
    @property
    def logger(self) -> AppLogger:
        return self.__logger__

    def check_table(self):
        from sqlalchemy.sql.schema import Table
        def __create__(table: Table):
            self.logger.i(f'check postgres table {table.name}')
            table.create(self.engine, checkfirst=True)
        
        print('pass create table!')
        # from .model import (
        #     ItemORM
        # )
        # __create__(ItemORM.__table__)
