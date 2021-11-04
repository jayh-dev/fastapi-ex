#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import time

from util import (logger)
import constants
from appenv import AppEnv

from http.client import responses
from fastapi import FastAPI, Request, Response
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

# --- app initializing ---
app = FastAPI(
    title=f'{AppEnv.APP_NAME.get()}',
    description='',
    version='0.0.1',
    debug=False,
    docs_url='/api/_doc',
    redoc_url='/api/_redoc',
)

app.logger = logger

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.middleware('http')
async def request_info(request: Request, call_next):
    start_time = time.time()
    response: Response = await call_next(request)
    logger.i('{} - "{} {}" {} {} - {}ms'.format(
        request.client.host, 
        request.method, 
        request.url.path, 
        response.status_code, 
        responses[response.status_code], 
        int((time.time() - start_time) * 1000000) / 1000
    ))
    return response

@app.exception_handler(Exception)
async def common_exception_handler(request, e):
    status_code, content = 500, {'detail': str(e)}
    
    if isinstance(e, NoResultFound):
        status_code, content = 404, {'detail': str(e)}
    elif isinstance(e, IntegrityError):
        status_code, content = 500, {'pg_code': e.orig.pgcode, 'detail': e.orig.pgerror}
    elif isinstance(e, HTTPException):
        status_code, content = e.status_code, {'detail': e.detail}

    logger.e('{} - "{} {}" {} {}'.format(
        request.client.host, 
        request.method, 
        request.url.path, 
        status_code,
        content
    ), trace=False)
    return JSONResponse(status_code=status_code, content=content)
# --- app initializing ---

# --- routers ---
@app.get('/', include_in_schema=False)
async def index():
    return AppEnv.APP_NAME.get()

@app.get('/_health_check', include_in_schema=False)
async def _health_check():
    return 'OK'

import router
from fastapi import Depends
from auth import auth_APIKey

__REST_PREFIX__ = '/rest'
app.include_router(
    router.RouterItem, 
    prefix=__REST_PREFIX__,
    tags=['Item'], 
    include_in_schema=constants.ITEM_IN_SCHEMA, 
    dependencies=[Depends(auth_APIKey)]
)
# --- routers ---



if __name__ == '__main__':
    import uvicorn

    # set $WEB_CONCURRENCY environment variable to set multiple workers
    uvicorn.run(app, host=AppEnv.HOST.get(), port=AppEnv.PORT.get())
