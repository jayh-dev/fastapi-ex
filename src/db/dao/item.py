#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from typing import List, Union
from sqlalchemy.orm.query import Query
from pydantic import parse_obj_as
from functools import lru_cache

from db import pg
from model.item import (
    Item, 
    ItemCreate,
    ItemUpdate
)
from ..model import ItemORM


def list(offset: int = 0, limit: int = 10) -> Union[int, List[Item]]:
    with pg.session as db:
        query: Query[ItemORM] = db.query(ItemORM)
        count = query.count()
        db_items: List[ItemORM] = query.order_by(ItemORM.created.desc()).limit(limit).offset(offset*limit).all()
        return count, parse_obj_as(List[Item], db_items)

def search_by_name(keyword: str, offset: int = 0, limit: int = 10) -> Union[int, List[Item]]:
    with pg.session as db:
        query: Query[ItemORM] = db.query(ItemORM).filter(ItemORM.name.like(f'%{keyword}%'))
        count = query.count()
        db_items: List[ItemORM] = query.order_by(ItemORM.created.desc()).limit(limit).offset(offset*limit).all()
        return count, parse_obj_as(List[Item], db_items)


#--- Basic CRUD
def create(item: ItemCreate) -> Item:
    with pg.session as db:
        db_item = ItemORM(**item.dict())
        db.add(db_item)
        db.flush()
        db.commit()
        db.refresh(db_item)
        return Item.from_orm(db_item)

@lru_cache(maxsize=10)
def retrieve_by_id(id: int) -> Item:
    with pg.session as db:
        db_item = db.query(ItemORM).filter(ItemORM.id == id).one()
        return Item.from_orm(db_item)

def patch(id: int, item: ItemUpdate) -> Item:
    with pg.session as db:
        db_item = db.query(ItemORM).filter(ItemORM.id == id).one()
        for k, v in item.dict().items():
            if v is not None: setattr(db_item, k, v)
        db.flush()
        db.commit()
        retrieve_by_id.cache_clear()
        return Item.from_orm(db_item)

def delete(id: int) -> Item:
    with pg.session as db:
        db_item = db.query(ItemORM).filter(ItemORM.id == id).one()
        db.delete(db_item)
        db.flush()
        db.commit()
        retrieve_by_id.cache_clear()
        return Item.from_orm(db_item)
#--- Basic CRUD
