#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from typing import List, Union
from datetime import datetime
from pydantic import parse_obj_as
from functools import lru_cache

from model.item import (
    Item,
    ItemCreate,
    ItemUpdate
)

from ..data_item import Data
__data__ = Data()

def list(offset: int = 0, limit: int = 10) -> Union[int, List[Item]]:
    with __data__ as db:
        count = db.count
        db_items = db.listInRange((offset * limit), ((offset+1) * limit))
        return count, parse_obj_as(List[Item], db_items)

def search_by_name(keyword: str, offset: int = 0, limit: int = 10) -> Union[int, List[Item]]:
    with __data__ as db:
        count, db_items = db.searchByName(keyword, (offset * limit), ((offset+1) * limit))
        return count, parse_obj_as(List[Item], db_items)


#--- Basic CRUD
def create(item: ItemCreate) -> Item:
    with __data__ as db:
        db_item = db.add(item)
        return parse_obj_as(Item, db_item)

@lru_cache(maxsize=10)
def retrieve_by_id(id: int) -> Item:
    print('hits database!', id)
    with __data__ as db:
        db_item = db.getById(id)
        return parse_obj_as(Item, db_item)

def patch(id: int, item: ItemUpdate) -> Item:
    with __data__ as db:
        db_item = db.update(id, item)
        retrieve_by_id.cache_clear()
        return parse_obj_as(Item, db_item)

def delete(id: int) -> Item:
    with __data__ as db:
        db_item = db.delete(id)
        retrieve_by_id.cache_clear()
        return parse_obj_as(Item, db_item)
#--- Basic CRUD
