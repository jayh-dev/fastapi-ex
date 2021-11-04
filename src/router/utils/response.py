#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from typing import TypeVar, Generic, Union, List
from pydantic import BaseModel
from pydantic.generics import GenericModel
from fastapi.responses import Response, JSONResponse

ResponseTypeItem = TypeVar('ResponseTypeItem')

class ResponseItem(GenericModel, Generic[ResponseTypeItem]):
    item: ResponseTypeItem = None
    extra: dict = None
    
    def __init__(self, item: ResponseTypeItem = None, **kwargs):
        super().__init__(item=item, extra=kwargs if kwargs else None)

    def response(self):
        return {**self.dict(exclude_none=True, exclude={'extra'}), **(self.extra if self.extra else {})}

class ResponseItems(GenericModel, Generic[ResponseTypeItem]):
    count: int = None
    items: List[ResponseTypeItem] = None
    extra: dict = None
    
    def __init__(self, count: int = None, items: List[ResponseTypeItem] = None, **kwargs):
        super().__init__(count=count, items=items, extra=kwargs if kwargs else {})

    def response(self):
        return {**self.dict(exclude_none=True, exclude={'extra'}), **(self.extra if self.extra else {})}

ResponseItemUnionType = Union[ResponseItem, ResponseItems]
def response_item_ok(item: ResponseItemUnionType = None, status_code: int = 200):
    if item: return JSONResponse(content=item.response(), status_code=status_code)
    return Response(status_code=status_code)

def response_item_ok_c(item: ResponseItemUnionType = None):
    return response_item_ok(item, 200)
def response_item_ok_r(item: ResponseItemUnionType = None):
    return response_item_ok(item, 200)
def response_item_ok_u(item: ResponseItemUnionType = None):
    return response_item_ok(item, 200)
def response_item_ok_d(item: ResponseItemUnionType = None):
    return response_item_ok(item if item else None, 200 if item else 204)


class ResponseCount(BaseModel):
    count: int = None
    extra: dict = None
    
    def __init__(self, count: int = None, **kwargs):
        super().__init__(count=count, extra=kwargs if kwargs else None)

    def response(self):
        return {**self.dict(exclude_none=True, exclude={'extra'}), **(self.extra if self.extra else {})}

def response_count_ok(item: ResponseCount = None, status_code: int = 200):
    if item: return JSONResponse(content=item.response(), status_code=status_code)
    return Response(status_code=status_code)
