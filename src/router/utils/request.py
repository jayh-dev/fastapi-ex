#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from fastapi import Query
from fastapi.exceptions import HTTPException


__LIMIT_MAX__ = 100
class CommonParametersPaging:
    def __init__(
        self, 
        offset: int = Query(0, ge=0),
        limit: int = Query(default=10, ge=1, le=__LIMIT_MAX__)
    ):
        self.__offset__ = offset
        self.__limit__ = limit
    
    @property
    def offset(self):
        if self.__offset__ < 0: raise HTTPException(400, '"offset" must be greater than or equal 0')
        return self.__offset__
    
    @property
    def limit(self):
        if self.__limit__ < 1 or self.__limit__ > __LIMIT_MAX__: raise HTTPException(400, f'"limit" must be range 1 to {__LIMIT_MAX__}')
        return self.__limit__

__SEARCH_KEYWORD_MIN_LEN__ = 2
class CommonParametersSearchByKeyword(CommonParametersPaging):
    def __init__(
        self, 
        offset: int = Query(0, ge=0),
        limit: int = Query(default=10, ge=1, le=__LIMIT_MAX__),
        keyword: str = Query(..., min_length=__SEARCH_KEYWORD_MIN_LEN__, description=f'More then {__SEARCH_KEYWORD_MIN_LEN__} characters')
    ):
        super().__init__(offset=offset, limit=limit)
        self.__keyword__ = keyword
    
    @property
    def keyword(self):
        if not self.__keyword__: raise HTTPException(400, f'"keyword" is missing')
        elif len(self.__keyword__) < __SEARCH_KEYWORD_MIN_LEN__: raise HTTPException(400, f'"keyword must be at least {__SEARCH_KEYWORD_MIN_LEN__} characters')
        return self.__keyword__
