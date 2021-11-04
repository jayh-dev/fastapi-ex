# FastApi Example

### Files
- init.sql  
    > generate data sample on postgresql.
- Dockerfiles/
    - Dockerfile-gunicorn
        > gunicorn
    - Dockerfile-pyinstaller
        > binary using pyinstaller
    - Dockerfile-pyinstaller-nginx
        > binary using pyinstaller & nginx proxy

---
### Environment Variables
- APP_ID
- APP_NAME
- APP_MODE
    > - dev
    > - prod
- DATA_SOURCE
    > - cache
    > - postgresql
- LOG_DIR
- LOG_LEVEL
    > - FATAL
    > - ERROR
    > - WARN
    > - INFO
    > - DEBUG
- HOST (default 127.0.0.1)
- PORT (default 8080)
- if DATA_SOURCE == 'postgresql'
    - PG_HOST
    - PG_PORT
    - PG_USER
    - PG_PASS
    - PG_DATABASE

---
### Execute
```
> cd src
> HOST=0.0.0.0 PORT=8080 python main.py
or
> uvicorn --host=0.0.0.0 --port=8080 main:app
```

---
