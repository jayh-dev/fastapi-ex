#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from fastapi import Request, Depends
from fastapi.exceptions import HTTPException


# --- APIKey Based Authorization
from fastapi.security.api_key import APIKeyBase, APIKeyHeader

__APIKEY_NAME__ = 'API_KEY'
__APIKEYS__ = {
    'testapikey': {
        'http_method_scope': ['*']
    }
}
__APIKEY_SECURITY__ = APIKeyHeader(name=__APIKEY_NAME__, scheme_name='API KEY', auto_error=False)

def auth_APIKey(request: Request, api_key: APIKeyBase = Depends(__APIKEY_SECURITY__)):
    if not api_key:
        raise HTTPException(401, f'{__APIKEY_NAME__} required')
    
    if api_key not in __APIKEYS__.keys():
        raise HTTPException(401, f'Not authorized ApiKey')
    
    auth = __APIKEYS__[api_key]
    if 'http_method_scope' not in auth:
        raise HTTPException(405, f'Method \'{request.method}\' not allowed')

    http_method_scope = auth['http_method_scope']
    if '*' not in http_method_scope:
        if request.method.lower() not in http_method_scope:
            raise HTTPException(405, f'Method \'{request.method}\' not allowed')
# --- APIKey Based Authorization

