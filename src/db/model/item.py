#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from sqlalchemy import Column, BIGINT, VARCHAR, TIMESTAMP, text

from . import _ModelBase

class ItemORM(_ModelBase):
    __tablename__ = 'item'
    __table_args__ = {'comment': 'Item'}

    id = Column(BIGINT, primary_key=True, autoincrement=True, comment='Database ID')
    name = Column(VARCHAR(128), unique=True, nullable=False, comment='Name')
    description = Column(VARCHAR(256), nullable=True, server_default='', comment='Description')
    created = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), comment='Created Timestamp')
