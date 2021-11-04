#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from router.utils import ResponseItem
from fastapi import APIRouter, Depends

from model.item import (
    Item,
    ItemCreate,
    ItemUpdate,
)

from .utils import *

from appenv import AppEnv
from constants import DataSources
data_source = AppEnv.DATA_SOURCE.get()
if data_source == DataSources.POSTGRESQL:
    from db.dao import DaoItem
else:
    from cache.dao import DaoItem


_router = APIRouter(prefix='/item')

@_router.get('/list', summary='Get List', response_model=ResponseItems[Item])
async def list(common_prms: CommonParametersPaging = Depends(CommonParametersPaging)):
    count, result = DaoItem.list(offset=common_prms.offset, limit=common_prms.limit)
    return response_item_ok_r(item=ResponseItems(items=result, count=count))


@_router.get('/serarch/name', summary='Search By Name', response_model=ResponseItems[Item])
async def list(common_prms: CommonParametersSearchByKeyword = Depends(CommonParametersSearchByKeyword)):
    count, result = DaoItem.search_by_name(offset=common_prms.offset, limit=common_prms.limit, keyword=common_prms.keyword)
    return response_item_ok_r(item=ResponseItems(items=result, count=count))


#--- Basic CRUD
@_router.post('', summary='Create Item', response_model=ResponseItem[Item])
async def create(item: ItemCreate):
    result = DaoItem.create(item)
    return response_item_ok_c(item=ResponseItem(item=result))

@_router.get('/{id}', summary='Get Item', response_model=ResponseItem[Item])
async def retrive(id: int):
    result = DaoItem.retrieve_by_id(id)
    return response_item_ok_r(item=ResponseItem(item=result))

@_router.patch('/{id}', summary='Update Item', response_model=ResponseItem[Item])
async def patch(id: int, item: ItemUpdate):
    result = DaoItem.patch(id, item)
    return response_item_ok_u(item=ResponseItem(item=result))

@_router.delete('/{id}', summary='Delete Item', status_code=204)
async def delete(id: int):
    DaoItem.delete(id)
    return response_item_ok_d(None)
#--- Basic CRUD
