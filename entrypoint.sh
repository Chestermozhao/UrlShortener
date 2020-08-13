#!/bin/bash

exec gunicorn --max-requests 100000 --max-requests-jitter 2000 -w 2 -t 25 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 url_shortener.main:app
