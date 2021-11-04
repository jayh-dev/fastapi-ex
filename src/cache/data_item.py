#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from fastapi.exceptions import HTTPException
from datetime import datetime
from typing import List, Union
from pydantic import parse_obj_as
from model.item import (
    Item,
    ItemCreate,
    ItemUpdate,
)


class Data:
    __data__ = [
        {'id': 1,  'name': 'Item01', 'description': 'Item01 Description', 'created': datetime.strptime('2021-10-28 14:33:10', '%Y-%m-%d %H:%M:%S') },
        {'id': 2,  'name': 'Item02', 'description': 'Item02 Description', 'created': datetime.strptime('2021-10-28 14:33:11', '%Y-%m-%d %H:%M:%S') },
        {'id': 3,  'name': 'Item03', 'description': 'Item03 Description', 'created': datetime.strptime('2021-10-28 14:33:12', '%Y-%m-%d %H:%M:%S') },
        {'id': 4,  'name': 'Item04', 'description': 'Item04 Description', 'created': datetime.strptime('2021-10-28 14:33:13', '%Y-%m-%d %H:%M:%S') },
        {'id': 5,  'name': 'Item05', 'description': 'Item05 Description', 'created': datetime.strptime('2021-10-28 14:33:14', '%Y-%m-%d %H:%M:%S') },
        {'id': 6,  'name': 'Item06', 'description': 'Item06 Description', 'created': datetime.strptime('2021-10-28 14:33:15', '%Y-%m-%d %H:%M:%S') },
        {'id': 7,  'name': 'Item07', 'description': 'Item07 Description', 'created': datetime.strptime('2021-10-28 14:33:16', '%Y-%m-%d %H:%M:%S') },
        {'id': 8,  'name': 'Item08', 'description': 'Item08 Description', 'created': datetime.strptime('2021-10-28 14:33:17', '%Y-%m-%d %H:%M:%S') },
        {'id': 9,  'name': 'Item09', 'description': 'Item09 Description', 'created': datetime.strptime('2021-10-28 14:33:18', '%Y-%m-%d %H:%M:%S') },
        {'id': 10, 'name': 'Item10', 'description': 'Item10 Description', 'created': datetime.strptime('2021-10-28 14:33:19', '%Y-%m-%d %H:%M:%S') },
        {'id': 11, 'name': 'Item11', 'description': 'Item11 Description', 'created': datetime.strptime('2021-10-28 14:33:20', '%Y-%m-%d %H:%M:%S') },
        {'id': 12, 'name': 'Item12', 'description': 'Item12 Description', 'created': datetime.strptime('2021-10-28 14:33:21', '%Y-%m-%d %H:%M:%S') },
        {'id': 13, 'name': 'Item13', 'description': 'Item13 Description', 'created': datetime.strptime('2021-10-28 14:33:22', '%Y-%m-%d %H:%M:%S') },
        {'id': 14, 'name': 'Item14', 'description': 'Item14 Description', 'created': datetime.strptime('2021-10-28 14:33:23', '%Y-%m-%d %H:%M:%S') },
        {'id': 15, 'name': 'Item15', 'description': 'Item15 Description', 'created': datetime.strptime('2021-10-28 14:33:24', '%Y-%m-%d %H:%M:%S') },
        {'id': 16, 'name': 'Item16', 'description': 'Item16 Description', 'created': datetime.strptime('2021-10-28 14:33:25', '%Y-%m-%d %H:%M:%S') },
        {'id': 17, 'name': 'Item17', 'description': 'Item17 Description', 'created': datetime.strptime('2021-10-28 14:33:26', '%Y-%m-%d %H:%M:%S') },
        {'id': 18, 'name': 'Item18', 'description': 'Item18 Description', 'created': datetime.strptime('2021-10-28 14:33:27', '%Y-%m-%d %H:%M:%S') },
        {'id': 19, 'name': 'Item19', 'description': 'Item19 Description', 'created': datetime.strptime('2021-10-28 14:33:28', '%Y-%m-%d %H:%M:%S') },
        {'id': 20, 'name': 'Item20', 'description': 'Item20 Description', 'created': datetime.strptime('2021-10-28 14:33:29', '%Y-%m-%d %H:%M:%S') },
    ][::-1]
    __id__ = __data__[0]['id']

    def __init__(self):
        pass

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        pass

    @property
    def nextId(self):
        self.__id__ += 1
        return self.__id__
    
    @property
    def count(self):
        return len(self.__data__)
    
    def getById(self, id) -> dict:
        for row in self.__data__:
            if row['id'] == id:
                return row
        raise HTTPException(404, f'not found item id {id}')
    
    def listInRange(self, idx_from, idx_to) -> List[dict]:
        return self.__data__[idx_from : idx_to]
    
    def searchByName(self, keyword, idx_from, idx_to) -> Union[int, List[dict]]:
        ret = []
        for v in self.__data__:
            if keyword in v['name']: ret.append(v)
        return len(ret), ret[idx_from : idx_to]
    
    def add(self, v: ItemCreate) -> dict:
        row = {'id': self.nextId, 'created': datetime.now(), **v.dict()}
        self.__data__.insert(0, row)
        return row
    
    def update(self, id: int, v: ItemUpdate) -> dict:
        row = self.getById(id)
        row.update(v.dict())
        return row
    
    def delete(self, id: int) -> dict:
        row = self.getById(id)
        self.__data__.remove(row)
        return row
