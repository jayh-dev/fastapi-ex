#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base

class ModelBase(object):
    pass

_ModelBase = declarative_base(cls=ModelBase)

from .item import ItemORM

