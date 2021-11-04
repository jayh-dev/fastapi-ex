#/usr/bin/env python3
#-*- encoding: utf-8 -*-

from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime
from .utils import validator_datetime

'''
    id: int
    name: str
    description: Optional[str] = None
    created: datetime
'''
class ItemBase(BaseModel):
    description: Optional[str] = None
    
    class Config:
        title = 'Item Base Model'
        orm_mode = True


class Item(ItemBase):
    id: int
    name: str
    created: datetime
    
    class Config:
        title = 'Item Retrieve Model'
        orm_mode = True

    @validator('created')
    def dt_parser(cls, v):
        return validator_datetime(v)


class ItemCreate(ItemBase):
    name: str

    class Config:
        title = 'Item Create Model'

class ItemUpdate(ItemBase):
    pass

    class Config:
        title = 'Item Update Model'
